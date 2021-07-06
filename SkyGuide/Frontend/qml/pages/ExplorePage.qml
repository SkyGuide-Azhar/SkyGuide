import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5
import "../controls"



Rectangle
{
    id: pageBgRec
    color: "#273139"

    Rectangle {
        id: raRec
        height: 40
        color: "#00000000"
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.topMargin: 130
        anchors.rightMargin: 60
        anchors.leftMargin: 50
        CustomeEntry
        {
            id: raTimeEntry
            anchors.left: parent.left
            anchors.right: raSepRec.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            labelTxt: "RA in time"
            txtFieldTxt: "enter the right assension in time \"h m s\""
            anchors.leftMargin: 0
            anchors.topMargin: 0

        }
        Rectangle
        {
            id: raSepRec

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
            id: raDegEntry
            anchors.left: raSepRec.right
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.topMargin: 0
            anchors.rightMargin: 15
            anchors.leftMargin: 0
            labelTxt: "RA in degree"
            txtFieldTxt: "enter the right assension in degree"
            anchors.bottomMargin: 0
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
        anchors.horizontalCenter: parent.horizontalCenter

        btnImageWidth: 20

        anchors.topMargin: 90

        btnImage: "../../images/svg_images/telescope.svg"
        btnTxt: "Send to mount"
        font.pointSize: 13
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:1000;width:640}
}
##^##*/
