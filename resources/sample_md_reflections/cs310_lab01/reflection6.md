# Report by

## Planning, due on January 27th, 2020 by 11am

### Timeline

| Timeline  | Tasks |
| ----------- | ----------- |
|   1.28    |    make sure get all needed parts   |
|   1.29    |    start adding humidity sensor     |
|   1.31    |    start adding the second sensor   |
|   2.3     |    start adding the third sensor    |
|   2.5     |    start adding the audio output    |
|   2.6     |    find a plant and conitue working on the output   |
|   2.7     |    finish     |

### Hardware

- Arduino board DUE

- humidity, temperature, light sensor, audio player, micro sd card..etc

`https://maker.pro/arduino/projects/arduino-audio-player`

## Arduino Project

Describe the application you have chosen to develop and provide a motivation for
why it is a useful application. Include  references of all sources you have used
throughout this project (URLs are sufficient).

The project I designed suppose to build a refelx agent, talking plant, by reading
in several values through temperature sensor, humidity sensor, light intensity
sensor, and sound sensor. The SD card would store some `.wav` audio files. These
audio can be played through the speaker when certain conditional logic has met.

## Agent

Explain the characteristics/attributes of your agent, what makes it an agent
(within the discussed course content), what makes it rational, what type of an
agent it is, and what is its environment task (PEAS).

As a relex agent, my talking plant uses Sound, Light, Humidity, Temperature as
inputs, and different audio sounds as outputs.

Input Section source code:

```
  int light_value = analogRead(lightsensor);
  int sound_value = analogRead(soundsensor);
  int humidity_value = analogRead(humiditysensor);
  sensors.requestTemperatures(); //Collecting temp data
```

Output Section 1: in text:

```
  light = light_value * 0.0976;// percentage calculation
  Serial.println("___________________");
  Serial.print("Light=");
  Serial.println(light);
  Serial.print("Sound=");
  Serial.println(sound_value,DEC);
  Serial.print("Temperature=");
  Serial.println(sensors.getTempCByIndex(0));
  Serial.print("Humidity=");
  Serial.println(humidity_value);
  Serial.println("___________________");
```

Output Section 2: in audio:

```
  if (light >= 100) {
    Serial.println("Uhh it's too much light!");
      // open wave file from sdcard
  File myFile1 = SD.open("toomuchlight.wav");
  playmusic(myFile1);
  }
  else if (light < 10) {
    Serial.println("Uhh it's too dark!");
    File myFile2 = SD.open("notenoughlight.wav");
    playmusic(myFile2);
  }
  if (sound_value < 500 || sound_value > 1000) {
    Serial.println("I hear sound!");
    File myFile3 = SD.open("hearsound.wav");
    playmusic(myFile3);
  }
  if (sensors.getTempCByIndex(0) != -127) {
    Serial.println("I feel temperature!");
    File myFile4 = SD.open("fixedbug.wav");
    playmusic(myFile4);
  }
  if (humidity_value > 100 ) {
    Serial.println("That's enough, that's enough!");
    File myFile5 = SD.open("toomuchwater.wav");
    playmusic(myFile5);
  }
  if (humidity_value > 50 && humidity_value < 100) {
    Serial.println("I got some water!");
    File myFile6 = SD.open("water.wav");
    playmusic(myFile6);
  }
```

The use of conditional logic allows my agent to make rational decisions.
With a specific input, it will provide a specific output. The in text output
in depends on all input values read by sensors. The audio output will occur
when some of the input values make expected changes.

## Challenges and Learning Experiences

Discuss any challenges you have encountered during the work on this lab and
describe what have you learned.

The engineering part is more difficult than the coding part especially when I
have some background in C already but have no background in electrical
engineering. I have faced severl difficulties when I am trying to connect parts
to the arduino board. The wires have different types such as GND, Power, Signal,
and I have to search online to find for a specific part and the wire setting for
this part. Additionally, I realize the Micrio SD Adaptor I have is not the one
for arduino, it is for PC or other product which can read in chips. Therefore,
I could not connect audio file I have stored in the Micro SD card to the arduino
board. The temperature sensor also has some problem. It seems like many people
also faced the issue of using temperature sensor on Arduino DUE, such that the
value will always be -127 and it would not change. However, some people got it
work.

## Ethical Benefits and Implications

In this section, drawing on class discussions and readings, answer the following
questions

1.What entities, businesses, organizations do you envision developing the type of
the application you have chosen to develop?

The environmental science would like to use this for researching. In agriculture,
it can be used for warning the farmers especially some plants are very sensitive.

2.Who are the intended users of this technology?

Farmers, households who is interested in having plants at home, ES researchers.

3.Who is not supposed to use this technology?

People who is allergy to plants and do not want a plant.

4.How can the application developed in this lab cause harm?

It is difficult to cause harm since it only has limited ability. However, if people
who is not supposed to use it and still used it, it may cause harm.

5.What solutions could be implemented to avoid the harm or to fix the harm described
above?

Warning sign to not allow people who has allergy to use.

## Team Work

Describe the details of your team working strategy, specifically explain how
did you complete this work as a team and describe the specific contributions
of each team member.

I don't have any other team members.
