import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5
import "../controls"



Rectangle
{
    id: pageBgRec
    color: "#273139"

    function searchOpp ()
    {
        if(searchNameTxtField.text.length > 0)
        {
            if(itemComboBox.currentText == "Star")
                backend.getSearchResult("stars", searchNameTxtField.text)
            else if(itemComboBox.currentText == " Constellation")
                backend.getSearchResult("constellations", searchNameTxtField.text)
            else if(itemComboBox.currentText == "Nebula")
                backend.getSearchResult("nebulas", searchNameTxtField.text)
            else if(itemComboBox.currentText == " Supernova remnants")
                backend.getSearchResult("supernova_remnants", searchNameTxtField.text)
            else if(itemComboBox.currentText == " Solar system object")
                backend.getSearchResult("solar_sys", searchNameTxtField.text)
        }
    }

    Rectangle {
        id: typeRec
        width: 630
        height: 50
        color: "#00000000"
        anchors.top: parent.top
        anchors.horizontalCenterOffset: -30
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
                resultRec.visible = sendToMountBtn.visible = notFoundRec.visible = false

                if(itemComboBox.currentText == "Star")
                {
                    itemComboBox.width = 150
                    comboText.horizontalAlignment = Text.AlignHCenter

                }
                else if(itemComboBox.currentText == " Constellation")
                {
                    itemComboBox.width = 150
                    comboText.horizontalAlignment = Text.AlignLeft
                }
                else if(itemComboBox.currentText == "Nebula")
                {
                    itemComboBox.width = 150
                    comboText.horizontalAlignment = Text.AlignHCenter
                }
                else if(itemComboBox.currentText == " Supernova remnants")
                {
                    itemComboBox.width = 200
                    comboText.horizontalAlignment = Text.AlignLeft
                }
                else if(itemComboBox.currentText == " Solar system object")
                {
                    itemComboBox.width = 200
                    comboText.horizontalAlignment = Text.AlignLeft
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

                color:"#ffffffff"
                text: itemComboBox.currentText
            }

            model: ListModel {
                    id: model
                    ListElement { text: "Star" }
                    ListElement { text: " Constellation" }
                    ListElement { text: "Nebula" }
                    ListElement { text: " Supernova remnants" }
                    ListElement { text: " Solar system object" }
                }


            background: Rectangle
            {
                color: "#00000000"

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
                text: qsTr("Select the object type :-")
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
    TextField
    {
        id: searchNameTxtField
        height: 40

        color: "#ffffff"
        anchors.left: parent.left
        anchors.right: searchBtn.left
        anchors.top: typeRec.bottom
        anchors.rightMargin: 60

        font.pointSize: 12

        anchors.leftMargin: 80
        anchors.topMargin: 30

        placeholderText: qsTr("enter the object's name")
        placeholderTextColor: "#838383"

        background: Rectangle
        {
            anchors.fill: parent

            border.color:"#838383"

            color: "#2c313c"
            radius: 10
        }

        selectByMouse: true
        selectedTextColor: "#FFFFFF"
        selectionColor: "#ff007f"

        Keys.onReturnPressed: searchOpp()
        Keys.onEnterPressed: searchOpp()
    }

    InfoButton
    {
        id: searchBtn
        width: 110
        height: 40
        anchors.right: parent.right
        anchors.top: typeRec.bottom
        anchors.rightMargin: 45
        anchors.topMargin: 30

        btnImageWidth: 20

        btnImage: "../../images/svg_images/search-interface-symbol.svg"
        btnTxt: "Search"
        font.pointSize: 13

        onClicked: searchOpp()

    }

    Rectangle
    {
        id: notFoundRec
        height: 70
        color: "#00000000"

        visible: false

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: searchNameTxtField.bottom
        anchors.rightMargin: 50
        anchors.leftMargin: 50
        anchors.topMargin: 150

        Label
        {
            id: notFoundMsg

            color: "#aaaaff"
            text:  if(itemComboBox.currentText == " Constellation")
                   {
                       "The entered constellation name is incorrect."
                   }
                   else if(itemComboBox.currentText == " Solar system object")
                   {
                       "Unfortunately, The entered solar system object is not in SkyGuide database."
                   }
                   else if (isNetDown)
                   {
                       "Internet connection is needed to perform the search."+"\n\n"
                       +"Kindly check your internet connection and try again."
                   }

                   else
                   {
                       "This "+ itemComboBox.currentText +" is not in SkyGuide database."+"\n\n"
                     +"You can navigate to the Add page to add a new item to SkyGuide database."
                   }

            anchors.verticalCenter: parent.verticalCenter

            anchors.horizontalCenter: parent.horizontalCenter

            font.bold: true
            font.italic: true
            font.weight: Font.ExtraLight
            font.family: "Times New Roman"
            font.pointSize: 15
        }

    }
        InfoButton
        {
            id: sendToMountBtn
            width: 155

            visible: false

            anchors.top: resultRec.bottom
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.bottomMargin: 5

            btnImageWidth: 20

            anchors.topMargin: 15

            btnImage: "../../images/svg_images/telescope.svg"
            btnTxt: "Send to mount"
            font.pointSize: 13

            onClicked:
            {
                backend.sendToMount_Search()
            }
        }

        Rectangle
        {
            id: resultRec
            color: "#1d2128"
            radius: 10

            visible: false

            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: searchBtn.bottom
            anchors.bottom: parent.bottom
            anchors.rightMargin: 40
            anchors.leftMargin: 40
            anchors.bottomMargin: 60
            anchors.topMargin: 50

            ScrollView {
                id: resutlScrollView

                anchors.fill: parent

                anchors.rightMargin: 15
                anchors.leftMargin: 15
                anchors.bottomMargin: 15
                anchors.topMargin: 15
                clip: true

                Text
                {
                    id: scrollText
                    color: "#ffffff"
                    anchors.fill: parent


                    font.family: "Times New Roman"
                    font.weight: Font.ExtraLight
                    font.pointSize: 15


                }

            }
        }
        property bool isNetDown: false
        Connections
        {
            target: backend

            function onSearchStatus (searchStatus)
            {
                sendToMountBtn.visible = searchStatus

                resultRec.visible = searchStatus

                notFoundRec.visible = !searchStatus
            }

            function onSearchResult(searchResult)
            {
                scrollText.text = searchResult

                if(searchResult === "Net is down")
                    isNetDown = true
                else
                    isNetDown = false

            }
        }


}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:0.75;height:700;width:750}
}
##^##*/
