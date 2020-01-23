%% Section 1
audFile = "ELE725_lab1.wav";

aud = audioread(audFile);
info = audioinfo(audFile);

player = audioplayer(aud, fs);

play(player);

% we got close jon

%% Section 2
N=10;
audFile = "ELE725_lab1.wav";
outFile = "output.wav";

[aud, fs] = audioread(audFile);

downsample(audFile, outFile, N, 1);