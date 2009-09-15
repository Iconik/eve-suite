//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, vJAXB 2.1.3 in JDK 1.6 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2009.04.30 at 05:11:01 PM CEST 
//


package model.api.corporation.assetlist;

import java.math.BigInteger;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for anonymous complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;sequence>
 *         &lt;element ref="{}rowset" minOccurs="0"/>
 *       &lt;/sequence>
 *       &lt;attribute name="flag" use="required" type="{http://www.w3.org/2001/XMLSchema}integer" />
 *       &lt;attribute name="itemID" use="required" type="{http://www.w3.org/2001/XMLSchema}integer" />
 *       &lt;attribute name="locationID" type="{http://www.w3.org/2001/XMLSchema}integer" />
 *       &lt;attribute name="quantity" use="required" type="{http://www.w3.org/2001/XMLSchema}integer" />
 *       &lt;attribute name="singleton" use="required" type="{http://www.w3.org/2001/XMLSchema}integer" />
 *       &lt;attribute name="typeID" use="required" type="{http://www.w3.org/2001/XMLSchema}integer" />
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "rowset"
})
@XmlRootElement(name = "row")
public class Row {

    protected Rowset rowset;
    @XmlAttribute(required = true)
    protected BigInteger flag;
    @XmlAttribute(required = true)
    protected BigInteger itemID;
    @XmlAttribute
    protected BigInteger locationID;
    @XmlAttribute(required = true)
    protected BigInteger quantity;
    @XmlAttribute(required = true)
    protected BigInteger singleton;
    @XmlAttribute(required = true)
    protected BigInteger typeID;

    /**
     * Gets the value of the rowset property.
     * 
     * @return
     *     possible object is
     *     {@link Rowset }
     *     
     */
    public Rowset getRowset() {
        return rowset;
    }

    /**
     * Sets the value of the rowset property.
     * 
     * @param value
     *     allowed object is
     *     {@link Rowset }
     *     
     */
    public void setRowset(Rowset value) {
        this.rowset = value;
    }

    /**
     * Gets the value of the flag property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getFlag() {
        return flag;
    }

    /**
     * Sets the value of the flag property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setFlag(BigInteger value) {
        this.flag = value;
    }

    /**
     * Gets the value of the itemID property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getItemID() {
        return itemID;
    }

    /**
     * Sets the value of the itemID property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setItemID(BigInteger value) {
        this.itemID = value;
    }

    /**
     * Gets the value of the locationID property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getLocationID() {
        return locationID;
    }

    /**
     * Sets the value of the locationID property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setLocationID(BigInteger value) {
        this.locationID = value;
    }

    /**
     * Gets the value of the quantity property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getQuantity() {
        return quantity;
    }

    /**
     * Sets the value of the quantity property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setQuantity(BigInteger value) {
        this.quantity = value;
    }

    /**
     * Gets the value of the singleton property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getSingleton() {
        return singleton;
    }

    /**
     * Sets the value of the singleton property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setSingleton(BigInteger value) {
        this.singleton = value;
    }

    /**
     * Gets the value of the typeID property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getTypeID() {
        return typeID;
    }

    /**
     * Sets the value of the typeID property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setTypeID(BigInteger value) {
        this.typeID = value;
    }

}
