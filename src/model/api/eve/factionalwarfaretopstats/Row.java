//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, vJAXB 2.1.3 in JDK 1.6 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2009.04.30 at 05:11:15 PM CEST 
//


package model.api.eve.factionalwarfaretopstats;

import java.math.BigInteger;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlSchemaType;
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
 *       &lt;attribute name="characterID" type="{http://www.w3.org/2001/XMLSchema}integer" />
 *       &lt;attribute name="characterName" type="{http://www.w3.org/2001/XMLSchema}anySimpleType" />
 *       &lt;attribute name="factionID" type="{http://www.w3.org/2001/XMLSchema}integer" />
 *       &lt;attribute name="factionName" type="{http://www.w3.org/2001/XMLSchema}anySimpleType" />
 *       &lt;attribute name="kills" type="{http://www.w3.org/2001/XMLSchema}integer" />
 *       &lt;attribute name="victoryPoints" type="{http://www.w3.org/2001/XMLSchema}integer" />
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

    @XmlAttribute
    protected BigInteger characterID;
    @XmlAttribute
    @XmlSchemaType(name = "anySimpleType")
    protected String characterName;
    @XmlAttribute
    protected BigInteger factionID;
    @XmlAttribute
    @XmlSchemaType(name = "anySimpleType")
    protected String factionName;
    @XmlAttribute
    protected BigInteger kills;
    @XmlAttribute
    protected BigInteger victoryPoints;

    /**
     * Gets the value of the characterID property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getCharacterID() {
        return characterID;
    }

    /**
     * Sets the value of the characterID property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setCharacterID(BigInteger value) {
        this.characterID = value;
    }

    /**
     * Gets the value of the characterName property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getCharacterName() {
        return characterName;
    }

    /**
     * Sets the value of the characterName property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setCharacterName(String value) {
        this.characterName = value;
    }

    /**
     * Gets the value of the factionID property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getFactionID() {
        return factionID;
    }

    /**
     * Sets the value of the factionID property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setFactionID(BigInteger value) {
        this.factionID = value;
    }

    /**
     * Gets the value of the factionName property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getFactionName() {
        return factionName;
    }

    /**
     * Sets the value of the factionName property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setFactionName(String value) {
        this.factionName = value;
    }

    /**
     * Gets the value of the kills property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getKills() {
        return kills;
    }

    /**
     * Sets the value of the kills property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setKills(BigInteger value) {
        this.kills = value;
    }

    /**
     * Gets the value of the victoryPoints property.
     * 
     * @return
     *     possible object is
     *     {@link BigInteger }
     *     
     */
    public BigInteger getVictoryPoints() {
        return victoryPoints;
    }

    /**
     * Sets the value of the victoryPoints property.
     * 
     * @param value
     *     allowed object is
     *     {@link BigInteger }
     *     
     */
    public void setVictoryPoints(BigInteger value) {
        this.victoryPoints = value;
    }

}
