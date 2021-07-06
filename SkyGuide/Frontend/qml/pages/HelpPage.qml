import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5
import "../controls"

Rectangle
{
    id: pageBgRec
    color: "#00000000"

    Label
    {
        id: tmpLabel
        text: "Help Page"
        color: "#ffffff"
        anchors.verticalCenter: parent.verticalCenter
        font.pointSize: 40
        anchors.horizontalCenter: parent.horizontalCenter


    }
}
