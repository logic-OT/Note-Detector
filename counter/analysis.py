import librosa
from statistics import mode,median_low
import numpy
from websocket.settings import BASE_DIR

def note_finder(data,meta_data):
        unique_key = meta_data['cookies']['file_name']
        print(unique_key)
        audio_path = str(BASE_DIR)+'/media/' + unique_key + '.wav'
        with open(audio_path ,'wb') as file:
            file.write(data)
            
        savedfile =  audio_path
        wave_file,samplerate = librosa.load(savedfile)
        pitches,_,l =   librosa.pyin(y=wave_file,
                            hop_length = 300,
                            sr=samplerate,
                            fmax=librosa.note_to_hz('C7'),
                            fmin=librosa.note_to_hz('A1'))
        pitches = list(pitches[~numpy.isnan(pitches)])

        note = pitches
        if note:   
                note = mode(librosa.hz_to_note(pitches))
                average = librosa.hz_to_note(median_low(pitches))
                print(note,average)
                if note != average:
                    return []
                return note
        return 'NaN'
    

