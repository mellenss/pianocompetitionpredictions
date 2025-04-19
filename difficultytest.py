from music21 import * 
from music21 import corpus, meter, tempo, expressions
import numpy as np
import pandas as pd
from collections import Counter

note_durations = {
    '32nd_and_shorter': 0.125,
    '16th': 0.25,
    'eighth': 0.5,
    'quarter': 1,
    'dotted quarter': 1.5,
    'half': 2,
    'dotted half': 3,
    'whole': 4
}
def analyze(filepath):
    score=converter.parse(filepath)
    flatscore=score.flatten()
    def notecount(flatscore):
       num_notes=0
       for elem in flatscore:
           if isinstance(elem, note.Note):
              num_notes += 1
           elif isinstance(elem, chord.Chord):
              num_notes += len(elem.pitches)
       return(num_notes)
    notecounts=notecount(flatscore)
    chords= [element for element in flatscore if isinstance(element, chord.Chord)]
    numberchords= len(chords)   
    def chordpitchdistances(chords):
        pitchdistances= []
        for i in range(len(chords)-1):
            firstchord= chords[i]
            secondchord= chords[i+1]
            rootInterval=interval.Interval(firstchord.root(),secondchord.root())
            pitchdistances.append(rootInterval.semitones)
        return(pitchdistances)
    pitchdistances=chordpitchdistances(chords)
    chord_abs_dis= [abs(dis) for dis in pitchdistances]
    meanchorddis= np.mean(chord_abs_dis)
    def chordtimedistances(chords):
        timedistances=[]
        for i in range(len(chords)-1):
            firstchord= chords[i]
            secondchord= chords[i+1]
            time_difference = secondchord.offset - firstchord.offset
            timedistances.append(time_difference) 
        return timedistances
    chordtimedistance=chordtimedistances(chords)
    meantimedistance=np.mean(chordtimedistance)
    key=flatscore.analyze('key')
    timesignature=flatscore.getElementsByClass(meter.TimeSignature)
    timesignaturechanges=len(timesignature)
    def findtrills(score):
        trills=0
        totalbeats=0
        for element in score.notesAndRests:
            if element.expressions:  # Check if the note has expressions
                for expr in element.expressions:
                    if isinstance(expr, expressions.Trill):  # Check if it's a trill
                        trills+= 1 
                        totalbeats+=element.quarterLength
        return [trills, totalbeats]
    trill_length=findtrills(flatscore)
    tempos= flatscore.getElementsByClass(tempo.MetronomeMark)
    sorted_tempos = sorted(tempos, key=lambda tm: tm.measureNumber)
    weighted_tempo=[]
    for i in range(len(sorted_tempos)):
        current_bpm = sorted_tempos[i].getQuarterBPM()
        current_measure = sorted_tempos[i].measureNumber
        if i < len(sorted_tempos) - 1:
            next_measure = sorted_tempos[i + 1].measureNumber
            duration = next_measure - current_measure
        else:
            # If this is the last tempo, assume it lasts to the end of the piece
            duration = score.highestTime
        weighted_tempo.append((current_bpm, duration))
    total_weight = sum(duration for _, duration in weighted_tempo)
    weighted_mean = (
    sum(bpm * duration for bpm, duration in weighted_tempo) / total_weight
    if total_weight != 0 else 0
    )
    num_measures = len(score.recurse().getElementsByClass('Measure'))
    duration_counter = Counter(note.duration.quarterLength for note in score.recurse().notes)
    def count_notes(score, duration_counter):
        note_counts= {}
        for name, duration in note_durations.items():
            if name=='32nd_and_shorter':
                note_counts[name]= sum(count for d, count in duration_counter.items() if d<=duration)
            else:
                note_counts[name]=duration_counter[duration]
        return note_counts
    notedict= count_notes(score,duration_counter)
    return{
        "numberofnotes": notecounts,
        "numberofchords": numberchords,
        "numberofmeasures": num_measures,
        "meandistancebetweenchords": meanchorddis,
        "meantimebetweenchords": meantimedistance,
        "key": key,
        "timechanges": timesignaturechanges,
        "trillslength": trill_length,
        "avgtempo" : weighted_mean,
        **notedict
    }


result=analyze('')

print(result)
