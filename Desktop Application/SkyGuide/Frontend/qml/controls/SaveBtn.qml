import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5

Button
{
    id: saveBtn

    property bool enableBtn: true

    property color defalutColor: if(enableBtn)
                                     "#64aafa"
                                 else
                                     "#526069"
    property color mouseOverColor: if(enableBtn)
                                       "#a3ceff"
                                   else
                                       "#526069"
    property color pressedColor: if(enableBtn)
                                     "#aaffff"
                                 else
                                     "#526069"
    background: Rectangle
    {
        anchors.fill: parent
        color: defalutColor
        radius:5

        Text
        {
            color: if(enableBtn)
                       "#000000"
                   else
                       "#8aa3b3"

            text: qsTr("Save")
            font.family: "Arial"
            font.pointSize: 13
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter

        }
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
