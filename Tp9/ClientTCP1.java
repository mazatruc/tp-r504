import java.io.*;
import java.net.*;

public class ClientTCP
{
	public static void main( String[] args )
	{
		try {
			Socket socket = new Socket( "localhost", 2016);
			DataOutputStream dOut = new DataOutputStream( socket.getOutputStream() );
			ded
		}
		catch( Exception ex )
		{
			System.out.println( "mother fuc" );
			ex.printStackTrace();
		}
	}
}