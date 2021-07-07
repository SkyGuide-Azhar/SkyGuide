import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5
import "../controls"



Rectangle
{
    id: pageBgRec
    color: "#273139"

    property string resultStr: ""

    Rectangle {
        id: raRec
        height: 40
        color: "#00000000"
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: resultRec.bottom
        anchors.topMargin: 30
        anchors.rightMargin: 60
        anchors.leftMargin: 50

        CustomeEntry
        {
            id: raEntry
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.rightMargin: 15
            anchors.bottomMargin: 0
            txtFieldTxt: "enter the right ascension in time \"h m s\" or in degrees"
            labelTxt: "Right Ascension"
            anchors.leftMargin: 0
            anchors.topMargin: 0

        }
    }

    Rectangle {
        id: decRec
        height: 40
        color: "#00000000"
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: raRec.bottom
        anchors.topMargin: 50
        anchors.rightMargin: 75
        anchors.leftMargin: 50
        CustomeEntry
        {
            id: decEntry
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            txtFieldTxt: "enter the declination"
            labelTxt: "Declination"
            anchors.leftMargin: 0
            anchors.topMargin: 0

        }
    }


    InfoButton
    {
        id: sendToMountBtn
        width: 155
        height: 40
        anchors.top: decRec.bottom
        anchors.topMargin: 50

        anchors.horizontalCenter: parent.horizontalCenter

        btnImageWidth: 20


        btnImage: "../../images/svg_images/telescope.svg"
        btnTxt: "Send to mount"
        font.pointSize: 13

        onClicked:
        {
            backend.expolreObject(raEntry.outputTxt, decEntry.outputTxt)
        }
    }

    Rectangle
    {
        id: resultRec

        width: 500
        height: 75
        color: "#00000000"

        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 50

        Label
        {
            id: resultLabel
            color: "#ffffff"
            anchors.fill: parent
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            font.bold: false
            font.italic: true
            font.weight: Font.ExtraLight
            font.family: "Times New Roman"
            font.pointSize: 15

            text: "Make sure to input correct data."
        }
    }
    Connections
    {
        target: backend

        function onExpolreResult (expolreResult)
        {
            resultLabel.text  = expolreResult
        }
    }

}



/*##^##
Designer {
    D{i:0;autoSize:true;height:1000;width:640}
}
##^##*/
