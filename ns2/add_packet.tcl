# 1. Create simulator
set ns [new Simulator]

# 2. Setup trace file for animation
set tracefile [open out.tr w]
$ns trace-all $tracefile

set namfile [open out.nam w]
$ns namtrace-all $namfile

# 3. Set the routing protocol to DSR (Link State behavior)
$ns node-config -routingAgent DSR

# 4. Create existing routers (nodes)
set r0 [$ns node]
set r1 [$ns node]
set r2 [$ns node]

# 5. Connect routers
$ns duplex-link $r0 $r1 1Mb 10ms DropTail
$ns duplex-link $r1 $r2 1Mb 10ms DropTail

# 6. Schedule the addition of a new router (r3)
set r3 [$ns node]
$ns at 3.0 "$ns duplex-link $r3 $r1 1Mb 10ms DropTail"
$ns at 3.5 "$ns duplex-link $r3 $r2 1Mb 10ms DropTail"

# 7. Setup traffic: r0 sends to r2
set udp [new Agent/UDP]
$ns attach-agent $r0 $udp

set null [new Agent/Null]
$ns attach-agent $r2 $null

$ns connect $udp $null

set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set packetSize_ 500
$cbr set interval_ 0.5

# Start sending traffic
$ns at 1.0 "$cbr start"
$ns at 7.0 "$cbr stop"

# 8. Finish simulation
$ns at 10.0 "finish"

proc finish {} {
    global ns tracefile namfile
    $ns flush-trace
    close $tracefile
    close $namfile
    exec nam out.nam &
    exit 0
}

# 9. Run the simulation
$ns run
