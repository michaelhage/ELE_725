close all
clear
%% Section 1 Audio File Properties
audFile = "ELE725_lab1.wav";

[aud, fs] = audioread(audFile);
info = audioinfo(audFile);
[X,Y] = size(aud);

player = audioplayer(aud, fs);

play(player);
%% Section 2 Sampling - Pre Filter
N=8;
audFile = "ELE725_lab1.wav";
outFile = "output_filter.wav";

[aud, fs] = audioread(audFile);

% Has Pre-Filtering
downsample(audFile, outFile, N, 1);

%% Section 2 Sampling - No Filter
N=8;
audFile = "ELE725_lab1.wav";
outFile = "output_nofilter.wav";
% Doesn't Have Pre-Filtering
downsample(audFile, outFile, N, 0);

%% Section 3 Quantization

%% Uniform Quantization

% Bit-Rate
N=8;

% Files
audFile = "ELE725_lab1.wav";
outFile = "output_quant.wav";

[MSE_U,uni_sig] = UniformQuant(audFile,outFile,N);

%    Plotting 
str = ["Original Audio(1)","Original Audio(2)",
        "Quantized Signal(1)","Quantized Signal(2)"];

plotx = {aud(:,1), aud(:,2), uni_sig(:,1), uni_sig(:,2)};

for i = 1:Y
    figure
    
    subplot(1,2,1);
    plot(plotx{2*i - 1});
    title(str{i,1});
    xlabel('Time');
    
    subplot(1,2,2)
    plot(plotx{2*i});
    title(str{i,2});
    xlabel('Time');
end

%% Mu-Law Qunatization

N=8;
Mu=100;

% Files
audFile = "ELE725_lab1.wav";
outFile = "output_mu.wav";

[MSE_M, mu_sig] = MulawQuant(audFile, outFile, N, Mu);

str = ["Original Audio(1)","Original Audio(2)"; 
        "Quantized Signal(1)", "Quantized Signal(2)"];
plotx = {aud(:,1), aud(:,2), mu_sig(:,1), mu_sig(:,2)};
    
for i = 1:2
   figure
        
   subplot(1,2,1);
   plot(plotx{2*i - 1});
   title(str{i,1});
   xlabel('Time');
        
   subplot(1,2,2)
   plot(plotx{2*i});
   title(str{i,2});
   xlabel('Time');
end

%% Comparisons

figure
hold on
plot(aud(100:300), 'g');
plot(uni_sig(100:300),'--.r');
plot(mu_sig(100:300),'--.b')
hold off
