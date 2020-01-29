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
    
    aud_interp(:,1) = interp(aud_down(:,1), N);
    aud_interp(:,2) = interp(aud_down(:,2), N);
    
%     Can reduce this to a single fft for each
    Aud1 = fft(aud(:,1));
    Aud2 = fft(aud(:,2));
    Aud_Down1 = fft(aud_down(:,1));
    Aud_Down2 = fft(aud_down(:,2));
    Aud_Interp1 = fft(aud_interp(:,1));
    Aud_Interp2 = fft(aud_interp(:,2));
    
    disp('Original Audio')
    sound(aud,fs)
    pause(5)
    disp('Downsampled Audio')
    sound(aud_down, fs/N)
    pause(5)
    disp('Interpolated Audio')
    sound(aud_interp,fs)
    
    plotx = {abs(Aud1), abs(Aud2), abs(Aud_Down1), abs(Aud_Down2), ...
        abs(Aud_Interp1), abs(Aud_Interp2)};
    str = {'Original Audio(1)', 'Original Audio(2)', ...
        'Downsampled Audio(1)','Downsampled Audio(2)', ...
        'Reconstructed Audio(1)', 'Reconstructed Audio(2)'};

    
    for i = 1:length(plotx)
        figure
        
        subplot(1,2,1);
        spectrogram(fftshift(plotx{i}));
        title(str{i});
        xlabel('Frequency');
        
        subplot(1,2,2)
        stem(fftshift(plotx{i}));
        title(str{i});
        xlabel('Frequency');
    end
    
    audiowrite(outFile, aud_down, fs/N);
end
