package model.api;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URISyntaxException;

import javax.xml.bind.JAXBException;

public class Control {
    public static Object apiControl(String dir, String file, int userID, String apiKey) {
	Object result = null;

	try {
	    Fetcher.fetch(URLs.staticURL+"/"+dir+"/"+file+URLs.xml+"?userID="+userID+"&apiKey="+apiKey,"Resources/API/User"+userID+"/"+dir+"/"+file+URLs.xml);
	} catch (URISyntaxException e1) {
	    // TODO Auto-generated catch block
	    e1.printStackTrace();
	} catch (IOException e1) {
	    // TODO Auto-generated catch block
	    e1.printStackTrace();
	}
	File file2 = new File("Resources/API/UserID "+userID+"/"+dir+"/"+file+URLs.xml);
	if(file2.canRead()) {
	    try {
		result = XMLMuncher.unmarshal("Resources/API/UserID "+userID+"/"+dir+"/"+file+URLs.xml, "api.account");
	    } catch (FileNotFoundException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	    } catch (JAXBException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	    }
	}
	return result;
    }
}
