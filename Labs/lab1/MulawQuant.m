function [MSE] = MuLawQuant(inFile, outFile, N, Mu)
%QUNA Summary of this function goes here
%   Detailed explanation goes here
[y, Fs] = audioread(inFile);
X_max = max(y(:,1));
abs_y = abs(y);
sign_y = sign(y);
quantized_signal = X_max*((log10(1+mu.*abs_y./X_max)) / (log10(1+mu))).*sign_y;
audiowrite('mu_quantized.wav', quantized_signal, Fs);
transformed_signal = UniformQuant('mu_quantized.wav', 'mu_UQ.wav', N);
abs_ts = abs(transformed_signal);
sign_ts = sign(transformed_signal);
reconstructed_signal = (X_max/mu)*(10.^((log10(1+mu)/X_max).*abs_ts) - 1).*sign_ts;
audiowrite(outFile, reconstructed_signal, Fs);
