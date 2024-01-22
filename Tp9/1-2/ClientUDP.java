import java.io.*;
import java.net.*;

public class ClientUDP
{
	byte[] data = s.getBytes();
	public static void main( String s = "Hello World" )
	{
		InetAddress addr = InetAddress.getLocalHost();
		System.out.println( "adresse=" +addr.getHostName() );
		
		DatagramPacket packet = new DatagramPacket( data, data.length, addr, 1234 );
		DatagramSocket sock = new DatagramSocket();
		sock.send(packet);
		sock.close();
	}
}