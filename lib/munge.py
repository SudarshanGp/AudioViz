import sys
sys.path.insert(2, '/usr/local/lib/python2.7/site-packages')

import wave
import struct
import numpy as np

N = 60 * 10000


def amplitudes(song):
    ''' Extract the amplitudes from a WAV file. '''
    # Read the .wav file
    # print("in amplites")
    # print(song)
    wavFile = wave.open(song + '.wav')
    # print(wavFile)
    # with wave.open('{}.wav'.format(song)) as wavFile:
        # Decompose it into bytes
    if wavFile.getnframes() < N * 2:
        raise ValueError('Wave file too short')
    frames = wavFile.readframes(N // 2)
    # Decode the bytes into a tuple of amplitudes of size 2n
    data = struct.unpack('%dh' % N, frames)
    return np.array(data)


def samples(X, n):
    ''' Equally split an array and average the samples. '''
    size = int(len(X) / n)
    samples = X.reshape(-1, size)
    means = samples.mean(1)
    return means


def differences(X, order):
    ''' Recursive function for computing differences. '''
    if order == 0:
        return X
    else:
        X = np.insert(X[1:] - X[:-1], 0, X[0])
        return(differences(X, order-1))


def moments(X):
    ''' Compute moments of an array. '''
    mean = X.mean()
    std = X.std()
    skewness = ((X - mean) ** 3).mean() / std ** 3
    kurtosis = ((X - mean) ** 4).mean() / std ** 4
    return {
        'mean': mean,
        'std': std,
        'skewness': skewness,
        'kurtosis': kurtosis
    }


def features(song, nbDifferences=[0, 1, 2], nbSamples=[1, 10, 100, 1000]):
    '''
    Convert a .wav file to numeric frames and extract
    information from the frames.
    '''
    print(song)
    features = {}
    frames = amplitudes(song)
    print("PRININT FRAMES")
    print(frames)
    print(len(frames))
    for d in nbDifferences:
        diffs = differences(frames, d)
        for s in nbSamples:
            samps = samples(diffs, s)
            moms = moments(samps)
            for m, array in moms.items():
                key = '{0}_differences_{1}_sample_{2}'.format(d, s, m)
                features[key] = array
    return features
