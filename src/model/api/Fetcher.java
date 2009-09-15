package model.api;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.ArrayList;

public class Fetcher {
    public static void fetch(String link, String output) throws URISyntaxException, IOException {
	URI uri = new URI(link);
	URL url = uri.toURL();
	InputStream is = url.openStream();
	InputStreamReader isr = new InputStreamReader(is);
	BufferedReader br = new BufferedReader(isr);
	String line;
	ArrayList<String> input = new ArrayList<String>();
	while((line=br.readLine())!=null) {
	    input.add(line);
	}

	File file = new File(output);
	file.createNewFile();
	FileWriter fw = new FileWriter(file);
	BufferedWriter bw = new BufferedWriter(fw);
	for(String out: input) {
	    bw.write(out);
	    bw.newLine();
	}

	bw.close();
    }
}
