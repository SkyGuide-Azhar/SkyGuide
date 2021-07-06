import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5
import "../controls"

Rectangle
{
    id: bgRec
    color: "#273139"


    CustomeEntry
    {
        id: nameEntry
        height: 40
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: addLabel.bottom

        anchors.rightMargin: 15

        txtFieldTxt: "enter the star's name (Required)"
        labelTxt: "Name"

        anchors.leftMargin: 0
        anchors.topMargin: 20

    }


    Rectangle {
        id: raDecRec
        height: 40
        color: "#00000000"
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: nameEntry.bottom
        anchors.topMargin: 15
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        CustomeEntry
        {
            id: raTimeEntry
            anchors.left: parent.left
            anchors.right: raDecSepRec.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            labelTxt: "RA in time"
            txtFieldTxt: "enter the right assension in time \"h m s\" (Required)"
            anchors.leftMargin: 0
            anchors.topMargin: 0
        }
        Rectangle
        {
            id: raDecSepRec

            width: 5
            color: "#00000000"
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 0
            anchors.topMargin: 0
            anchors.horizontalCenter: parent.horizontalCenter
        }

        CustomeEntry
        {
            id: decEntry
            anchors.left: raDecSepRec.right
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.topMargin: 0
            anchors.rightMargin: 15
            anchors.leftMargin: 0
            anchors.bottomMargin: 0
            txtFieldTxt: "enter the declination (Required)"
            labelTxt: "Declination"

        }
    }
    Rectangle {
        id: bayerConRec
        height: 40
        color: "#00000000"
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: raDecRec.bottom
        anchors.topMargin: 15
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        CustomeEntry
        {
            id: bayerEntry
            anchors.left: parent.left
            anchors.right: bayerConSepRec.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            txtFieldTxt: "enter the star's bayer name"
            labelTxt: "Bayer Name"
            anchors.leftMargin: 0
            anchors.topMargin: 0

        }
        Rectangle
        {
            id: bayerConSepRec

            width: 5
            color: "#00000000"
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 0
            anchors.topMargin: 0
            anchors.horizontalCenter: parent.horizontalCenter
        }

        CustomeEntry
        {
            id: conEntry
            anchors.left: bayerConSepRec.right
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.topMargin: 0
            anchors.rightMargin: 15
            anchors.leftMargin: 0
            labelTxt: "Constellation"
            txtFieldTxt: "enter the constellation name or IAU"
            anchors.bottomMargin: 0
        }
    }

    Rectangle {
        id: colorIdxDistRec
        height: 40
        color: "#00000000"
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: bayerConRec.bottom
        anchors.topMargin: 15
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        CustomeEntry
        {
            id: colorIdxEntry
            anchors.left: parent.left
            anchors.right: colorIdxDistSepRec.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            labelTxt: "Color Index"
            txtFieldTxt: "enter the color index"
            anchors.leftMargin: 0
            anchors.topMargin: 0

        }
        Rectangle
        {
            id: colorIdxDistSepRec

            width: 5
            color: "#00000000"
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 0
            anchors.topMargin: 0
            anchors.horizontalCenter: parent.horizontalCenter
        }

        CustomeEntry
        {
            id: distEntry
            anchors.left: colorIdxDistSepRec.right
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.topMargin: 0
            anchors.rightMargin: 15
            anchors.leftMargin: 0
            labelTxt: "Distance"
            txtFieldTxt: "enter the distance in light years"
            anchors.bottomMargin: 0
        }
    }

    Rectangle {
            id: magSpectRec

            height: 40
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: colorIdxDistRec.bottom
            anchors.topMargin: 15
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            CustomeEntry
            {
                id: magEntry
                anchors.left: parent.left
                anchors.right: magSpectSepRec.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.rightMargin: 0
                anchors.bottomMargin: 0
                txtFieldTxt: "enter the magnitude"
                labelTxt: "Magnitude"
                anchors.leftMargin: 0
                anchors.topMargin: 0

            }
            Rectangle
            {
                id: magSpectSepRec

                width: 5
                color: "#00000000"
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 0
                anchors.topMargin: 0
                anchors.horizontalCenter: parent.horizontalCenter
            }

            CustomeEntry
            {
                id: spectEntry
                anchors.left: magSpectSepRec.right
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.topMargin: 0
                anchors.rightMargin: 15
                anchors.leftMargin: 0
                labelTxt: "Spectrum"
                txtFieldTxt: "enter the spectrum"
                anchors.bottomMargin: 0
            }
        }
    SaveBtn
    {
        id: saveBtn
        width: 75
        height: 40
        anchors.right: clearBtn.left
        anchors.top: magSpectRec.bottom
        anchors.rightMargin: 50
        anchors.topMargin: 50

        enableBtn: ((nameEntry.outputTxt.length   != 0)&&
                    (raTimeEntry.outputTxt.length != 0)&&
                    (decEntry.outputTxt.length    != 0))

        onClicked: if(enableBtn)
                      backend.addUserStar(nameEntry.outputTxt,
                                          raTimeEntry.outputTxt,
                                          decEntry.outputTxt,
                                          entryCheck(distEntry.outputTxt),
                                          entryCheck(magEntry.outputTxt),
                                          entryCheck(spectEntry.outputTxt),
                                          entryCheck(colorIdxEntry.outputTxt),
                                          entryCheck(bayerEntry.outputTxt),
                                          entryCheck(conEntry.outputTxt))

    }

    function entryCheck(entry)
    {
        if(entry.length > 0)
            return entry
        return "N/A"
    }

    ClearBtn
    {
        id: clearBtn

        width: 90
        height: 40
        anchors.right: parent.right
        anchors.top: magSpectRec.bottom
        anchors.rightMargin: 15
        anchors.topMargin: 50

        onClicked:
        {
            nameEntry.clear()
            raTimeEntry.clear()
            decEntry.clear()
            distEntry.clear()
            magEntry.clear()
            spectEntry.clear()
            colorIdxEntry.clear()
            bayerEntry.clear()
            conEntry.clear()

            addLabel.text = "Make sure to fill the required data."
        }
    }

    Label
    {
        id: addLabel
        height: 40
        text: "Make sure to fill the required data."
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        anchors.rightMargin: 15
        anchors.leftMargin: 20
        anchors.topMargin: 0

        color: "#ffffff"
        font.bold: false
        font.italic: true
        font.weight: Font.ExtraLight
        font.family: "Times New Roman"
        font.pointSize: 15
    }


    Connections
    {
        target: backend

        function onStarAddResult(message)
        {
            addLabel.text = message
        }
    }



}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.9;height:700;width:1000}
}
##^##*/
