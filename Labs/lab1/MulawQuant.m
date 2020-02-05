function [MSE, compand_sig] = MulawQuant(inFile, outFile, N, Mu)
%MULAWQUANT Summary of this function goes here
%   Detailed explanation goes here

    [aud, fs] = audioread(inFile);
    [X,Y] = size(aud);
    
    quant_sig = zeros(X,Y);
    compand_sig = zeros(X,Y);

    for i = 1:Y
       X_max(i) = max(abs(aud(:,i)));
       
       quant_sig(:,i) = X_max(i) .* sign(aud(:,i)) .* log10(1 + Mu.*abs(aud(:,i) ...
           ./X_max(i))) ./ log10(1+Mu);
    end
    
    audiowrite('mu_quantized.wav', quant_sig, fs);
    [MSE,t_sig] = UniformQuant('mu_quantized.wav', 'mu_UQ.wav', N);
    
    for i = 1:Y
       
        compand_sig(:,i) = X_max(i)./Mu .* (10.^(log10(1+Mu).*abs(t_sig(:,i)) ...
            ./X_max(i)) - 1) .* sign(t_sig(:,i));
    end
    
    for i = 1:Y
        MSE(i) = (1/X).*sum( (compand_sig(:,i) - aud(:,i)).^2 );
    end
    
end