%% Section 1 Audio File Properties
audFile = "ELE725_lab1.wav";

aud = audioread(audFile);
info = audioinfo(audFile);

player = audioplayer(aud, fs);

play(player);

% we got close jon

%% Section 2 Sampling
N=10;
audFile = "ELE725_lab1.wav";
outFile = "output.wav";

[aud, fs] = audioread(audFile);

% Has Pre-Filtering
downsample(audFile, outFile, N, 1);

pause(5);

% Doesn't Have Pre-Filtering
downsample(audFile, outFile, N, 0);

%% Section 3 Quantization
