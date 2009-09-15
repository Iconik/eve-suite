//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, vJAXB 2.1.3 in JDK 1.6 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2009.04.30 at 05:10:51 PM CEST 
//


package model.api.account;

import javax.xml.bind.JAXBElement;
import javax.xml.bind.annotation.XmlElementDecl;
import javax.xml.bind.annotation.XmlRegistry;
import javax.xml.namespace.QName;


/**
 * This object contains factory methods for each 
 * Java content interface and Java element interface 
 * generated in the api.account package. 
 * <p>An ObjectFactory allows you to programatically 
 * construct new instances of the Java representation 
 * for XML content. The Java representation of XML 
 * content can consist of schema derived interfaces 
 * and classes representing the binding of schema 
 * type definitions, element declarations and model 
 * groups.  Factory methods for each of these are 
 * provided in this class.
 * 
 */
@XmlRegistry
public class ObjectFactory {

    private final static QName _CurrentTime_QNAME = new QName("", "currentTime");
    private final static QName _CachedUntil_QNAME = new QName("", "cachedUntil");

    /**
     * Create a new ObjectFactory that can be used to create new instances of schema derived classes for package: api.account
     * 
     */
    public ObjectFactory() {
    }

    /**
     * Create an instance of {@link Result }
     * 
     */
    public Result createResult() {
        return new Result();
    }

    /**
     * Create an instance of {@link Eveapi }
     * 
     */
    public Eveapi createEveapi() {
        return new Eveapi();
    }

    /**
     * Create an instance of {@link Rowset }
     * 
     */
    public Rowset createRowset() {
        return new Rowset();
    }

    /**
     * Create an instance of {@link Row }
     * 
     */
    public Row createRow() {
        return new Row();
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link String }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "currentTime")
    public JAXBElement<String> createCurrentTime(String value) {
        return new JAXBElement<String>(_CurrentTime_QNAME, String.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link String }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "cachedUntil")
    public JAXBElement<String> createCachedUntil(String value) {
        return new JAXBElement<String>(_CachedUntil_QNAME, String.class, null, value);
    }

}
