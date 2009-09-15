//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, vJAXB 2.1.3 in JDK 1.6 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2009.04.30 at 05:11:09 PM CEST 
//


package model.api.corporation.shareholder;

import java.math.BigInteger;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlSchemaType;
import javax.xml.bind.annotation.XmlType;
import javax.xml.bind.annotation.adapters.CollapsedStringAdapter;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;


/**
 * <p>Java class for anonymous complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;attribute name="shareholderCorporationID" use="required" type="{http://www.w3.org/2001/XMLSchema}integer" />
 *       &lt;attribute name="shareholderCorporationName" use="required" type="{http://www.w3.org/2001/XMLSchema}NCName" />
 *       &lt;attribute name="shareholderID" use="required" type="{http://www.w3.org/2001/XMLSchema}integer" />
 *       &lt;attribute name="shareholderName" use="required" type="{http://www.w3.org/2001/XMLSchema}NCName" />
 *       &lt;attribute name="shares" use="required" type="{http://www.w3.org/2001/XMLSchema}integer" />
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "")
@XmlRootElement(name = "row")
public class Row {

    @XmlAttribute(required = true)
    protected BigInteger shareholderCorporationID;
    @XmlAttribute(required = true)
    @XmlJavaTypeAdapter(CollapsedStringAdapter.class)
    @XmlSchemaType(name = "NCName")
    protected String shareholderCorporationName;
    @XmlAttribute(required = true)
    protected BigInteger shareholderID;
    @XmlAttribute(required = true)
    @XmlJavaTypeAdapter(CollapsedStringAdapter.class)
    @XmlSchemaType(name = "NCName")
    protected String shareholderName;
    @XmlAttribute(required = true)
    protected BigInteger shares;

    /**
     * Gets the value of the shareholderCorporationID property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getShareholderCorporationID() {
        return shareholderCorporationID;
    }

    /**
     * Sets the value of the shareholderCorporationID property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setShareholderCorporationID(BigInteger value) {
        this.shareholderCorporationID = value;
    }

    /**
     * Gets the value of the shareholderCorporationName property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getShareholderCorporationName() {
        return shareholderCorporationName;
    }

    /**
     * Sets the value of the shareholderCorporationName property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setShareholderCorporationName(String value) {
        this.shareholderCorporationName = value;
    }

    /**
     * Gets the value of the shareholderID property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getShareholderID() {
        return shareholderID;
    }

    /**
     * Sets the value of the shareholderID property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setShareholderID(BigInteger value) {
        this.shareholderID = value;
    }

    /**
     * Gets the value of the shareholderName property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getShareholderName() {
        return shareholderName;
    }

    /**
     * Sets the value of the shareholderName property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setShareholderName(String value) {
        this.shareholderName = value;
    }

    /**
     * Gets the value of the shares property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getShares() {
        return shares;
    }

    /**
     * Sets the value of the shares property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setShares(BigInteger value) {
        this.shares = value;
    }

}
