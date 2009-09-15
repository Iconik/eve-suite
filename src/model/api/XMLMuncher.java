package model.api;

import java.io.File;
import java.io.FileNotFoundException;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;

public class XMLMuncher {
    public static Object unmarshal(String path, String pack) throws JAXBException, FileNotFoundException {
	final JAXBContext jaxbContext = JAXBContext.newInstance(pack);
        final Unmarshaller unmarshaller = jaxbContext.createUnmarshaller();
        final Object eveapi = unmarshaller.unmarshal(new File(path));
        return eveapi;
    }
    
    /*public static Eveapi eatAccount() throws FileNotFoundException, JAXBException {
	Eveapi eveapi = unmarshal("bin/api"+URLs.account+URLs.characterList,"api.account");
	System.out.println();
	return eveapi;
    }*/
}
