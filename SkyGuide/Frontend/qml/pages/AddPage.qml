import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5
import "../controls"

Rectangle
{
    id: bgRec
    color: "#273139"


    Rectangle {
        id: typeRec
        width: 630
        height: 50
        color: "#00000000"
        anchors.top: parent.top
        anchors.topMargin: 35
        anchors.horizontalCenter: parent.horizontalCenter

        ComboBox {
            id: itemComboBox

            width: 150
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.rightMargin: 15
            anchors.bottomMargin: 5
            anchors.topMargin: 5
            displayText:""

            onCurrentTextChanged:
            {
                if(itemComboBox.currentText == "Star")
                {
                      itemComboBox.width = 150
                      comboText.horizontalAlignment = Text.AlignHCenter
                      getDataStackView.push(Qt.resolvedUrl("../controls/getNewStarData.qml"))
                }
                else if(itemComboBox.currentText == "Nebula")
                {
                      itemComboBox.width = 150
                      comboText.horizontalAlignment = Text.AlignHCenter
                      getDataStackView.push(Qt.resolvedUrl("../controls/getNewNebulaData.qml"))
                }
                else if(itemComboBox.currentText == " Supernova remnants")
                {
                      itemComboBox.width = 200
                      comboText.horizontalAlignment = Text.AlignLeft
                      getDataStackView.push(Qt.resolvedUrl("../controls/getNewSupernovaData.qml"))
                }
            }

            Text
            {
                id: comboText
                height: 30
                anchors.fill: parent
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.weight: Font.ExtraLight
                font.italic: false
                font.family: "Times New Roman"
                font.pointSize: 15
                color:"#000000"
                text: itemComboBox.currentText
            }

            model: ListModel {
                    id: model
                    ListElement { text: "Star" }
                    ListElement { text: "Nebula" }
                    ListElement { text: " Supernova remnants" }
                }


            background: Rectangle
            {
                color: "#64aafa"
                border.color: "#688888"
                radius: 10
            }
        }

        Label
        {
            id: itemTypeLabel

            Text
            {
                anchors.fill: parent
                color: "#bdd0e6"
                text: qsTr("Select the item type :-")
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.family: "Times New Roman"
                font.pointSize: 15

            }

            anchors.left: parent.left
            anchors.right: itemComboBox.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 5
            anchors.rightMargin: 50

            anchors.leftMargin: 15
            anchors.topMargin: 5


        }


    }

    Rectangle {
        id: getDataRec
        color: "#00000000"
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: typeRec.bottom
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 40

        StackView {
            id: getDataStackView
            anchors.fill: parent
            anchors.rightMargin: 100
            anchors.leftMargin: 100
            initialItem: Qt.resolvedUrl("../controls/getNewStarData.qml")
            clip: true
        }
    }


}
