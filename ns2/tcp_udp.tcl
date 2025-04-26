# 1. Create the simulator
set ns [new Simulator]

# 2. Create a file to save the animation
set nf [open out.nam w]
$ns namtrace-all $nf

# 3. Create network nodes
set n0 [$ns node]  ;# Source for file transfer
set n1 [$ns node]  ;# Destination for file transfer
set n2 [$ns node]  ;# Source for video streaming
set n3 [$ns node]  ;# Destination for video streaming

# 4. Connect the nodes
$ns duplex-link $n0 $n1 1Mb 10ms DropTail
$ns duplex-link $n2 $n3 1Mb 10ms DropTail

# 5. Set up TCP connection for File Transfer
set tcp [new Agent/TCP]
$ns attach-agent $n0 $tcp

set sink [new Agent/TCPSink]
$ns attach-agent $n1 $sink

$ns connect $tcp $sink

# Create a file transfer application
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP

# 6. Set up UDP connection for Video Streaming
set udp [new Agent/UDP]
$ns attach-agent $n2 $udp

set null [new Agent/Null]
$ns attach-agent $n3 $null

$ns connect $udp $null

# Create a video streaming application (CBR - Constant Bit Rate)
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set packetSize_ 1000
$cbr set interval_ 0.05

# 7. Start the applications
$ns at 0.5 "$ftp start"    ;# Start FTP at 0.5 seconds
$ns at 1.0 "$cbr start"    ;# Start CBR (Video Stream) at 1.0 seconds

# 8. Stop the simulation
$ns at 5.0 "$ftp stop"
$ns at 5.0 "$cbr stop"
$ns at 5.0 "finish"

proc finish {} {
    global ns nf
    $ns flush-trace
    close $nf
    exit 0
}

# 9. Run the simulation
$ns run
