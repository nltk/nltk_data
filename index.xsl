<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="/nltk_data">
        <HTML>
            <HEAD>
                <TITLE>NLTK Data</TITLE>
            </HEAD>
            <BODY bgcolor="white" text="navy">
                <H1>NLTK Corpora</H1>
                <P>NLTK has built-in support for dozens of corpora and trained models, as listed below.
                To use these within NLTK we recommend that you use the NLTK corpus downloader,
                <TT>&gt;&gt;&gt; nltk.download()</TT></P>
		<P>Please consult the README file included with each
		corpus for further information.</P>
                <OL>
                <xsl:for-each select="//packages/package">
                    <LI><I><xsl:value-of select="@name"/></I>
                        [<xsl:element name="a">
                            <xsl:attribute name="href">
                                <xsl:value-of select="@url"/>                                
                            </xsl:attribute>
                            download
                        </xsl:element>
                        |<xsl:element name="a">
                            <xsl:attribute name="href">
                                <xsl:value-of select="@webpage"/>                                
                            </xsl:attribute>
                            source
                        </xsl:element>]
                        <BR/>
                        id: <tt><xsl:value-of select="@id"/></tt>;
                        size: <xsl:value-of select="@size"/>;
                        author: <xsl:value-of select="@author"/>;
                        copyright: <xsl:value-of select="@copyright"/>;
                        license: <xsl:value-of select="@license"/>;
                        <P/>
                    </LI>
                </xsl:for-each>
                </OL>
                <HR/>
                <A href="http://www.nltk.org">Natural Language Toolkit</A>
            </BODY>
        </HTML>
    </xsl:template>
</xsl:stylesheet>
