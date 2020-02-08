function [MSE, compand_sig] = MulawQuant(inFile, outFile, N, Mu)
%MULAWQUANT Summary of this function goes here
%   Detailed explanation goes here

    [aud, fs] = audioread(inFile);
    [X,Y] = size(aud);
    
    compress_sig = zeros(X,Y);
    quant_sig = zeros(X,Y);
    compand_sig = zeros(X,Y);

    for i = 1:Y
       X_max(i) = max(abs(aud(:,i)));
       
       compress_sig(:,i) = X_max(i) .* sign(aud(:,i)) .* log10(1 + Mu.*abs(aud(:,i) ./X_max(i))) ./ log10(1+Mu);
    end
    
    for i = 1:Y
       v_max = max(compress_sig(:,i));
       v_min = min(compress_sig(:,i));
       
       stepsize(i) = (v_max - v_min)/2.^N;
    end
    
    %     Quantize the signal
    for i = 1:Y
       quant_sig(:,i) = round(compress_sig(:,i) / stepsize(i) );
       X_max_q(i) = max(abs(quant_sig(:,i)));
    end
    
    for i = 1:Y
       
        compand_sig(:,i) = X_max(i)./Mu .* (10.^(log10(1+Mu).*abs(quant_sig(:,i)) ...
            ./X_max_q(i)) - 1) .* sign(quant_sig(:,i));
    end
    
    for i = 1:Y
        MSE(i) = (1/X).*sum( (compand_sig(:,i) - aud(:,i)).^2 );
    end
    
    audiowrite(outFile, compand_sig, fs);
    
end