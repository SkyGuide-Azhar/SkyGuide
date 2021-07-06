import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5


Rectangle
{
    property string labelTxt: "Label"
    property string txtFieldTxt: "enter something,,,"
    property string outputTxt: entryTxtField.text
    property string txtFieldDefaulttxt: entryTxtField.placeholderText

    function clear()
    {
        entryTxtField.remove(0,outputTxt.length)
    }

    color: "#00000000"

    Label
    {
        id: entryLabel
        width: 120
        color: "#ffffff"

        text: labelTxt
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom

        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter

        font.pointSize: 12
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        anchors.topMargin: 0
    }


    TextField
    {
        id: entryTxtField

        color: "#ffffff"
        anchors.left: entryLabel.right
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom

        font.pointSize: 10

        anchors.rightMargin: 0
        anchors.leftMargin: 10
        anchors.bottomMargin: 0
        anchors.topMargin: 0


        selectByMouse: true
        selectedTextColor: "#FFFFFF"
        selectionColor: "#ff007f"


        placeholderText: txtFieldTxt
        placeholderTextColor: "#ffffff"

        background: Rectangle
        {
            anchors.fill: parent

            border.color:"#ffffff"

            color: "#2c313c"
            radius: 8
        }
    }


}

/*##^##
Designer {
    D{i:0;autoSize:true;height:50;width:640}
}
##^##*/
