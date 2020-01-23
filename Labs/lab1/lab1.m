%% Section 1

aud = audioread("ELE725_lab1.wav");
info = audioinfo("ELE725_lab1.wav");

player = audioplayer(aud, fs);

play(player);

% we got close jon

%% Section 2
N=10;

aud_down = downsample(aud, N);

player_down = audioplayer(aud_down, fs);

play(player_down);