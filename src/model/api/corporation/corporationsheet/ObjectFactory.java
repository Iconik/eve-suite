//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, vJAXB 2.1.3 in JDK 1.6 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2009.04.30 at 05:11:02 PM CEST 
//


package model.api.corporation.corporationsheet;

import java.math.BigDecimal;
import java.math.BigInteger;
import javax.xml.bind.JAXBElement;
import javax.xml.bind.annotation.XmlElementDecl;
import javax.xml.bind.annotation.XmlRegistry;
import javax.xml.bind.annotation.adapters.CollapsedStringAdapter;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;
import javax.xml.namespace.QName;


/**
 * This object contains factory methods for each 
 * Java content interface and Java element interface 
 * generated in the api.corporation.corporationsheet package. 
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

    private final static QName _Color3_QNAME = new QName("", "color3");
    private final static QName _TaxRate_QNAME = new QName("", "taxRate");
    private final static QName _CachedUntil_QNAME = new QName("", "cachedUntil");
    private final static QName _CorporationID_QNAME = new QName("", "corporationID");
    private final static QName _CorporationName_QNAME = new QName("", "corporationName");
    private final static QName _Shape2_QNAME = new QName("", "shape2");
    private final static QName _Shape1_QNAME = new QName("", "shape1");
    private final static QName _CeoName_QNAME = new QName("", "ceoName");
    private final static QName _Shape3_QNAME = new QName("", "shape3");
    private final static QName _StationID_QNAME = new QName("", "stationID");
    private final static QName _AllianceName_QNAME = new QName("", "allianceName");
    private final static QName _Url_QNAME = new QName("", "url");
    private final static QName _MemberCount_QNAME = new QName("", "memberCount");
    private final static QName _CurrentTime_QNAME = new QName("", "currentTime");
    private final static QName _Shares_QNAME = new QName("", "shares");
    private final static QName _Ticker_QNAME = new QName("", "ticker");
    private final static QName _Description_QNAME = new QName("", "description");
    private final static QName _GraphicID_QNAME = new QName("", "graphicID");
    private final static QName _AllianceID_QNAME = new QName("", "allianceID");
    private final static QName _Color2_QNAME = new QName("", "color2");
    private final static QName _StationName_QNAME = new QName("", "stationName");
    private final static QName _Color1_QNAME = new QName("", "color1");
    private final static QName _CeoID_QNAME = new QName("", "ceoID");
    private final static QName _MemberLimit_QNAME = new QName("", "memberLimit");

    /**
     * Create a new ObjectFactory that can be used to create new instances of schema derived classes for package: api.corporation.corporationsheet
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
     * Create an instance of {@link Logo }
     * 
     */
    public Logo createLogo() {
        return new Logo();
    }

    /**
     * Create an instance of {@link Row }
     * 
     */
    public Row createRow() {
        return new Row();
    }

    /**
     * Create an instance of {@link Rowset }
     * 
     */
    public Rowset createRowset() {
        return new Rowset();
    }

    /**
     * Create an instance of {@link Eveapi }
     * 
     */
    public Eveapi createEveapi() {
        return new Eveapi();
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "color3")
    public JAXBElement<BigInteger> createColor3(BigInteger value) {
        return new JAXBElement<BigInteger>(_Color3_QNAME, BigInteger.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigDecimal }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "taxRate")
    public JAXBElement<BigDecimal> createTaxRate(BigDecimal value) {
        return new JAXBElement<BigDecimal>(_TaxRate_QNAME, BigDecimal.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link String }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "cachedUntil")
    public JAXBElement<String> createCachedUntil(String value) {
        return new JAXBElement<String>(_CachedUntil_QNAME, String.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "corporationID")
    public JAXBElement<BigInteger> createCorporationID(BigInteger value) {
        return new JAXBElement<BigInteger>(_CorporationID_QNAME, BigInteger.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link String }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "corporationName")
    public JAXBElement<String> createCorporationName(String value) {
        return new JAXBElement<String>(_CorporationName_QNAME, String.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "shape2")
    public JAXBElement<BigInteger> createShape2(BigInteger value) {
        return new JAXBElement<BigInteger>(_Shape2_QNAME, BigInteger.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "shape1")
    public JAXBElement<BigInteger> createShape1(BigInteger value) {
        return new JAXBElement<BigInteger>(_Shape1_QNAME, BigInteger.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link String }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "ceoName")
    public JAXBElement<String> createCeoName(String value) {
        return new JAXBElement<String>(_CeoName_QNAME, String.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "shape3")
    public JAXBElement<BigInteger> createShape3(BigInteger value) {
        return new JAXBElement<BigInteger>(_Shape3_QNAME, BigInteger.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "stationID")
    public JAXBElement<BigInteger> createStationID(BigInteger value) {
        return new JAXBElement<BigInteger>(_StationID_QNAME, BigInteger.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link String }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "allianceName")
    public JAXBElement<String> createAllianceName(String value) {
        return new JAXBElement<String>(_AllianceName_QNAME, String.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link String }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "url")
    public JAXBElement<String> createUrl(String value) {
        return new JAXBElement<String>(_Url_QNAME, String.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "memberCount")
    public JAXBElement<BigInteger> createMemberCount(BigInteger value) {
        return new JAXBElement<BigInteger>(_MemberCount_QNAME, BigInteger.class, null, value);
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
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "shares")
    public JAXBElement<BigInteger> createShares(BigInteger value) {
        return new JAXBElement<BigInteger>(_Shares_QNAME, BigInteger.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link String }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "ticker")
    @XmlJavaTypeAdapter(CollapsedStringAdapter.class)
    public JAXBElement<String> createTicker(String value) {
        return new JAXBElement<String>(_Ticker_QNAME, String.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link String }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "description")
    public JAXBElement<String> createDescription(String value) {
        return new JAXBElement<String>(_Description_QNAME, String.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "graphicID")
    public JAXBElement<BigInteger> createGraphicID(BigInteger value) {
        return new JAXBElement<BigInteger>(_GraphicID_QNAME, BigInteger.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "allianceID")
    public JAXBElement<BigInteger> createAllianceID(BigInteger value) {
        return new JAXBElement<BigInteger>(_AllianceID_QNAME, BigInteger.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "color2")
    public JAXBElement<BigInteger> createColor2(BigInteger value) {
        return new JAXBElement<BigInteger>(_Color2_QNAME, BigInteger.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link String }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "stationName")
    public JAXBElement<String> createStationName(String value) {
        return new JAXBElement<String>(_StationName_QNAME, String.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "color1")
    public JAXBElement<BigInteger> createColor1(BigInteger value) {
        return new JAXBElement<BigInteger>(_Color1_QNAME, BigInteger.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "ceoID")
    public JAXBElement<BigInteger> createCeoID(BigInteger value) {
        return new JAXBElement<BigInteger>(_CeoID_QNAME, BigInteger.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link BigInteger }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "", name = "memberLimit")
    public JAXBElement<BigInteger> createMemberLimit(BigInteger value) {
        return new JAXBElement<BigInteger>(_MemberLimit_QNAME, BigInteger.class, null, value);
    }

}
