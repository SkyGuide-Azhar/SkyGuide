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

        txtFieldTxt: "enter the nebula's name (Required)"
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
            labelTxt: "Declination"
            txtFieldTxt: "enter the declination (Required)"
            anchors.bottomMargin: 0
        }
    }


    Rectangle {
        id: conDistRec
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
            id: conEntry
            anchors.left: parent.left
            anchors.right: conDistSepRec.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            labelTxt: "Constellation"
            txtFieldTxt: "enter the constellation name or IAU"
            anchors.leftMargin: 0
            anchors.topMargin: 0

        }
        Rectangle
        {
            id: conDistSepRec

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
            anchors.left: conDistSepRec.right
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
            id: dimRadRec

            height: 40
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: conDistRec.bottom
            anchors.topMargin: 15
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            CustomeEntry
            {
                id: dimEntry
                anchors.left: parent.left
                anchors.right: dimRadSepRec.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.rightMargin: 0
                anchors.bottomMargin: 0
                txtFieldTxt: "enter the dimensions"
                labelTxt: "Dimensions"
                anchors.leftMargin: 0
                anchors.topMargin: 0

            }
            Rectangle
            {
                id: dimRadSepRec

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
                id: radEntry
                anchors.left: dimRadSepRec.right
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.topMargin: 0
                anchors.rightMargin: 15
                anchors.leftMargin: 0
                labelTxt: "Raduis"
                txtFieldTxt: "enter the nebula's raduis"
                anchors.bottomMargin: 0
            }
        }
    SaveBtn
    {
        id: saveBtn
        width: 100
        height: 40
        anchors.right: clearBtn.left
        anchors.top: dimRadRec.bottom
        anchors.rightMargin: 50
        anchors.topMargin: 50

        enableBtn: ((nameEntry.outputTxt.length   != 0)&&
                    (raTimeEntry.outputTxt.length != 0)&&
                    (decEntry.outputTxt.length    != 0))


        onClicked: if(enableBtn)
                      backend.addUserNebula(nameEntry.outputTxt,
                                           raTimeEntry.outputTxt,
                                           decEntry.outputTxt,
                                           entryCheck(distEntry.outputTxt),
                                           entryCheck(dimEntry.outputTxt),
                                           entryCheck(radEntry.outputTxt),
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
        anchors.top: dimRadRec.bottom
        anchors.rightMargin: 15
        anchors.topMargin: 50

        onClicked:
        {
            nameEntry.clear()
            raTimeEntry.clear()
            decEntry.clear()
            distEntry.clear()
            dimEntry.clear()
            radEntry.clear()
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

        function onNebulaAddResult(message)
        {
            addLabel.text = message
        }
    }



}

/*##^##
Designer {
    D{i:0;autoSize:true;height:630;width:700}
}
##^##*/
