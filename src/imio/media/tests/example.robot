*** Settings ***
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Suite Setup  Suite Setup
Suite Teardown  Close all browsers


*** Test Cases ***
Site Administrator can add and view vimeo video
    Open add new menu
    ${status} =  Run Keyword And Return Status  Click Link
    ...  css=#plone-contentmenu-factories a.contenttype-media_link
    Input Text  form.widgets.IDublinCore.title  Vidéo
    Input Text  form.widgets.remoteUrl  http://vimeo.com/95988841
    Click button  id=form-buttons-save
    Go to  ${PLONE_URL}/video
    Page should contain  <iframe


*** Keywords ***
Suite Setup
    Open test browser
    Enable autologin as  Site Administrator
    Go to  ${PLONE_URL}
