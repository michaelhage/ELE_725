function out = downsample(in, N)
%DOWNSAMPLE Summary of this function goes here
%   Detailed explanation goes here
    
    out = in(1:N:end,:);

end

