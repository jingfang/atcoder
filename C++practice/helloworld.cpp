#include <iostream>

using namespace std;

int main(){
    cout << "Helloworld!" << endl;
    return 0;
}

/* xcrun: error: invalid active developer path (/Applications/Xcode.app/Contents/Developer), 
 missing xcrun at: /Applications/Xcode.app/Contents/Developer/usr/bin/xcrun
で困ってたけど、https://stackoverflow.com/questions/35009531/xcrun-error-active-developer-path-applications-xcode-app-contents-developer
の "Use this sudo xcode-select -switch /"を試したらうまくいった！　*/