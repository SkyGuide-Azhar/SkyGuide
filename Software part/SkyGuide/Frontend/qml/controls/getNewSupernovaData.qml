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
        anchors.topMargin: 15

    }

    CustomeEntry
    {
        id: raTimeEntry
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: nameEntry.bottom
        anchors.rightMargin: 15

        height: 40

        labelTxt: "RA in time"
        txtFieldTxt: "enter the right assension in time \"h m s\" (Required)"
        anchors.leftMargin: 0
        anchors.topMargin: 15

    }

    Rectangle {
        id: decFVFERec
        height: 40
        color: "#00000000"
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: raTimeEntry.bottom
        anchors.topMargin: 15
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        CustomeEntry
        {
            id: decEntry
            anchors.left: parent.left
            anchors.right: decFVFESepRec.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            txtFieldTxt: "enter the declination (Required)"
            labelTxt: "Declination"
            anchors.leftMargin: 0
            anchors.topMargin: 0

        }
        Rectangle
        {
            id: decFVFESepRec

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
            id: fVFEEntry
            anchors.left: decFVFESepRec.right
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.topMargin: 0
            anchors.rightMargin: 15
            anchors.leftMargin: 0
            labelTxt: "First visible"
            txtFieldTxt: "enter the first time it was visible form earth"
            anchors.bottomMargin: 0
        }
    }

    Rectangle {
        id: remnantDistRec
        height: 40
        color: "#00000000"
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: decFVFERec.bottom
        anchors.topMargin: 15
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        CustomeEntry
        {
            id: remnantEntry
            anchors.left: parent.left
            anchors.right: remnantDistSepRec.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            labelTxt: "Remnant"
            txtFieldTxt: "enter the remnant"
            anchors.leftMargin: 0
            anchors.topMargin: 0

        }
        Rectangle
        {
            id: remnantDistSepRec

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
            anchors.left: remnantDistSepRec.right
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


    SaveBtn
    {
        width: 100
        height: 40
        anchors.right: clearBtn.left
        anchors.top: remnantDistRec.bottom
        anchors.rightMargin: 50

        anchors.topMargin: 50

        enableBtn: ((nameEntry.outputTxt.length   != 0)&&
                    (raTimeEntry.outputTxt.length != 0)&&
                    (decEntry.outputTxt.length    != 0))
        onClicked: if(enableBtn)
                      backend.addUserSupernovaRemnant(nameEntry.outputTxt,
                                                      raTimeEntry.outputTxt,
                                                      decEntry.outputTxt,
                                                      entryCheck(distEntry.outputTxt),
                                                      entryCheck(fVFEEntry.outputTxt),
                                                      entryCheck(remnantEntry.outputTxt))

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
        anchors.top: remnantDistRec.bottom
        anchors.rightMargin: 15
        anchors.topMargin: 50

        onClicked:
        {
            nameEntry.clear()
            raTimeEntry.clear()
            decEntry.clear()
            distEntry.clear()
            fVFEEntry.clear()
            remnantEntry.clear()

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

        function onSupernovaRemnantAddResult(message)
        {
            addLabel.text = message
        }
    }

}



/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:1.1;height:480;width:700}
}
##^##*/
