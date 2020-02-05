function [MSE, quant_sig] = UniformQuant(inFile, outFile, N)
%QUNA Summary of this function goes here
%   Detailed explanation goes here

    [aud, fs] = audioread(inFile);
    [X,Y] = size(aud);
    
    quant_sig = zeros(X,Y);
    stepsize = zeros(Y,1);
    MSE = zeros(Y:1);
    
%     Calculate the stepsize
    for i = 1:Y
       v_max = max(aud(:,i));
       v_min = min(aud(:,i));
       
       stepsize(i) = (v_max - v_min)/2.^N;
    end
    
%     Quantize the signal
    for i = 1:Y
       quant_sig(:,i) = round(aud(:,i) / stepsize(i) );
    end
    
%     Reconstruct the qunatized signal
    for i = 1:Y
       quant_sig(:,i) = stepsize(i) * quant_sig(:,i);
    end
    
%     Mean Square Error
    for i = 1:Y
        MSE(i) = (1/X).*sum( (quant_sig(:,i) - aud(:,i)).^2 );
    end
    
%    Plotting 
    str = ["Original Audio(1)","Quantized Signal(1)"; 
        "Original Audio(2)", "Quantized Signal(2)"];
    
%     Output Audio
    audiowrite(outFile, quant_sig, fs);
end