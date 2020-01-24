function downsample(inFile, outFile, N, pf)
%DOWNSAMPLE Summary of this function goes here
%   Detailed explanation goes here
    
    [aud, fs] = audioread(inFile);
    [X,Y] = size(aud);
    
    aud_down = zeros(int16(X./N),Y);
    
    if(pf == true)
        aud_down(:,1) = decimate(aud(:,1), N, 2);
        aud_down(:,2) = decimate(aud(:,2), N, 2);
    else
        aud_down(:,1) = decimate(aud(:,1), N);
        aud_down(:,2) = decimate(aud(:,2), N);
    end
    
    sound(aud,fs)
    pause(5)
    sound(aud_down, fs/N)
    
    audiowrite(outFile, aud_down, fs/N);
    
    Aud1 = fft(aud(:,1));
    Aud2 = fft(aud(:,2));
    Aud_Down1 = fft(aud_down(:,1));
    Aud_Down2 = fft(aud_down(:,2));
    
    plotx = {abs(Aud1), abs(Aud2), abs(Aud_Down1), abs(Aud_Down2)};
    str = {'Original Audio(1)', 'Original Audio(2)', 'Downsampled Audio(1)', 'Downsampled Audio(2)'};

    figure
    for i = 1:length(plotx)
        subplot(2,length(plotx),i);
        spectrogram(fftshift(plotx{i}));
        title(str{i});
        xlabel('Frequency');
        
        subplot(2,length(plotx),i+3)
        plot(fftshift(plotx{i}));
        title(str{i});
        xlabel('Frequency');
    end
    

end

