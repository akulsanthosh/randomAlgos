set ns [new Simulator]
set nf [open out.nam w]
$ns nametrace-all $nf

set tf [open out.tr w]
$ns trace-all $tf

proc finish {} {
    global ns nf tf
    $ns flush-trace
    close $nf
    close $tf
    exec nam out.nam &
    exec awk -f packetDrop.awk out.tr &
    exec awk -f throughput.awk out.tr > out.gr
    exec xgraph out.gr
    exit 0
}

set n0 [$ns node]
set n1 [$ns node]

$ns duplex-link $n0 $n1 1Mb 10ms DropTail

$ns duplex-link-op $n2 $n3 queuePos 0.5

set tcp0 [new Agent/TCP]
$ns attach-agent $n0 $tcp0

set sink0 [new Agent/TCPSink]
$ns attach-agent $n1 $sink0

set udp0 [new Agent/UDP]
$ns attach-agent $n0 $udp0

set null0 [new Agent/Null]
$ns attach-agent $n1 $null0

set ftp0 [new Application/FTP]
$ftp0 attach-agent $n0

set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500
$cbr0 set interval_ 0.005
$cbr0 attach-agent $n0

$ns connect $tcp0 $sink0
$ns connect $udp0 $null0

$ns rtmodel-at 5.0 down $n0 $n1
$ns rtmodel-at 7.0 up $n0 $n1

$ns rtproto DV
$ns rtproto LS

$ns at 0.1 "cbr0 start"
$ns at 0.1 "ftp0 start"
$ns at 10.0 "ftp0 stop"
$ns at 10.0 "cbr0 stop"

$ns at 10.1 "finish"
$ns run

Array :-

$n($i)

Evaluate :-

[expr ($i+1)%7]

Loop :-

for {set i 0} {$i < 7} {incr i}{
    $ns duplex-link $n($i) $n([expr ($i+1)%7]) 1Mb 10ms DropTail
}

packetDrop.awk

#!/Usr/bin/awk

BEGIN{
    total_drop = 0;
}
{
    if($1 == "d"){
        total_drop += 1;
    }
}
END{
    printf("Total No of Packets dropped : %d/n",total_drop)
}

throughput.awk

#!/Usr/bin/awk

BEGIN{
    data = 0;
}
{
    if($1 == "r" && $4 == "2" && $5 == "tcp"){
        data += $6;
        print $2,data*0.8/$2/1000000

    }
}
END{
    
}