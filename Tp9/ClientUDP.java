import java.io.*;
import java.net.*;

public class ClientUDP
{
	public static void main()
	{
		String s = "Hello World";
		try {
			InetAddress addr = InetAddress.getLocalHost();
			System.out.println( "adresse = " + addr.getHostName() );
			byte[] data = s.getBytes();
			DatagramPacket packet = new DatagramPacket (data, data.length, addr, 1234 );
			DatagramSocket sock = new DatagramSocket();
			sock.send(packet);
			sock.close();
		}
	
		catch( Exception ex )
		{
			System.out.println( "mother fuc" );
			ex.printStackTrace();
		}
	}
}