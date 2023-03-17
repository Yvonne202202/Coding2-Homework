# Coding2-Homework

## OpenFrameworks 1: 
### Panopto:
https://ual.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=08d4b253-e94c-497a-a4f2-afc600d3f917&start=0

### Brief: 
I transferred my sound and signal processing project to openFrameworks. I use basic waveforms to create a range of sounds that continually changed. I added two sinewave oscillators of different frequenciestogether to make the sound fading in and out.
### Description
* ofxMaxi library is used.
* I defined three properties: oscillator1, oscillator2, myClock for changing the sound. 
```
    maxiOsc oscillator1;
    maxiOsc oscillator2;
    maxiClock myClock;
```
Sets up a maxiClock object called 'myClock'.The clock speed is set to 120 by using setTempo(). And the number of beats is set to 4 by setTicksPerBeat().
```
    for (int i = 0; i < ofGetWidth(); ++i) {
        waveform[i] = 0;
    }
    waveIndex = 0;
    
    // Maximilian audio stuff
    int sampleRate = 44100; /* Sampling Rate */
    int bufferSize= 512; /* Buffer Size. you have to fill this buffer with sound using the for loop in the audioOut method */
    ofxMaxiSettings::setup(sampleRate, 2, bufferSize);
    
    myClock.setTempo(120);
    myClock.setTicksPerBeat(4);
    // Setup ofSound
    ofSoundStreamSettings settings;
    settings.setOutListener(this);
    settings.sampleRate = sampleRate;
    settings.numOutputChannels = 2;
    settings.numInputChannels = 0;
    settings.bufferSize = bufferSize;
    soundStream.setup(settings);

```
* To make the sound more distinctive, the method sinewave() in maxiOsc is used. 
```
  for (int i = 0; i < output.getNumFrames(); ++i){
        myClock.ticker();
        if(myClock.tick && ofRandom(0.9)>0.7)
        {
            myFreq += 20;
        }
        else
        {
            myFreq -= 5;
        }
        output[i * outChannels] = oscillator1.coswave(myFreq*0.2*oscillator2.sinewave(0.01))* 0.5;
        output[i * outChannels + 1] = output[i * outChannels];
        
        //Hold the values so the draw method can draw them
        waveform[waveIndex] =  output[i * outChannels];
        if (waveIndex < (ofGetWidth() - 1)) {
            ++waveIndex;
        } else {
            waveIndex = 0;
        }
    }
```
*  Draw the waveform of the sound.
```
    ofTranslate(0, ofGetHeight()/2);
    ofSetColor(0, 255, 0);
    
    ofFill();
    ofDrawLine(0, 0, 1, waveform[1] * ofGetHeight()/2.); //first line
    for(int i = 1; i < (ofGetWidth() - 1); ++i) {
        ofDrawLine(i, waveform[i] * ofGetHeight()/2., i + 1, waveform[i+1] * ofGetHeight()/2.);
    }
```

## OpenFrameworks 2:
### Panopto:
https://ual.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=adcaaba7-6acc-4d0a-a877-afc600d3f8f8&start=0
### Brief: 
It's a team effort. We created a newboids class, which is a subclass of the boids class. It has a different look than the boids class, which we treat as two separate groups.
### Description
* Maximilian library is used.
* Three maxiSample objects are created using the Maximilian library, which are beat, loop, and chord. 
```
  audio.loadSample('loop.wav',loop);
  audio.loadSample('beat.wav',beat);
  audio.loadSample('chord.wav',chord);
```

## Python 1: 
### Panopto:
https://ual.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=4b405178-49fa-44d0-afc6-afc600d3f8f7&start=0

### Brief: 
I used Python 3.x with the packages NumPy and matplotlib. I loaded the two images in the img_align_celeba folder and visualized the difference between the two images.
### Description
* Maximilian library is used.
* Three maxiSample objects are created using the Maximilian library, which are beat, loop, and chord. 
```
  audio.loadSample('loop.wav',loop);
  audio.loadSample('beat.wav',beat);
  audio.loadSample('chord.wav',chord);
```

## Python 2:
### Panopto:
https://ual.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=db2200f7-d7a2-4709-82be-afc600d3f90e

### Brief: 
I took two images in the folder according to the tutorial and used TensorFlow to style one image.
### Description
* Maximilian library is used.
* Three maxiSample objects are created using the Maximilian library, which are beat, loop, and chord. 
```
  audio.loadSample('loop.wav',loop);
  audio.loadSample('beat.wav',beat);
  audio.loadSample('chord.wav',chord);
```
