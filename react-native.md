## React Native

```bash
# document: 
https://reactnative.dev/docs/environment-setup
```

### Download:
```bash
nodejs
vscode
```

### In Terminal:
```bash
# If you previously installed a global react-native-cli package, please remove it as it may cause unexpected issues:
npm uninstall -g react-native-cli @react-native-community/cli

npx react-native@latest init NameProject
cd NameProject
code .

npx react-native start
# connect to device (turn on USB debuging) and run:
npx react-native run-android
```

### React Navigation:
```bash
# document: 
https://reactnavigation.org/docs/getting-started

yarn add @react-navigation/native

# located in android/app/src/main/java/<your package name>/MainActivity.java and paste
@Override
protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(null);
}

# and make sure to add an import statement at the top of this file:
import android.os.Bundle;
```

### Maybe use Library:
```bash
yarn add react-native-vector-icons
yarn add @react-native-community/masked-view
yarn add react-native-gesture-handler
yarn add react-native-pager-view
yarn add react-native-paper
yarn add react-native-reanimated
yarn add react-native-safe-area-context
yarn add react-native-screens
yarn add react-native-tab-view
yarn add @react-navigation/bottom-tabs
yarn add react-navigation-drawer
yarn add @react-navigation/elements
yarn add @react-navigation/material-bottom-tabs
yarn add @react-navigation/material-top-tabs
yarn add @react-navigation/native-stack
yarn add @react-navigation/native
yarn add @react-navigation/stack
```

### Super Library :)))
```
yarn add react-native-vector-icons @react-native-community/masked-view react-native-gesture-handler react-native-pager-view react-native-paper react-native-reanimated react-native-safe-area-context react-native-screens react-native-tab-view @react-navigation/bottom-tabs react-navigation-drawer @react-navigation/elements @react-navigation/material-bottom-tabs react-navigation-drawer @react-navigation/elements @react-navigation/material-bottom-tabs @react-navigation/material-top-tabs @react-navigation/native-stack @react-navigation/native @react-navigation/stack
```

### Expo:
```bash
# install expo:
npm install --global expo-cli

# run app:
expo start
```

### Icon:
```bash
# document: 
https://github.com/oblador/react-native-vector-icons

# icon:
https://ionic.io/ionicons

# edit android/app/build.gradle and add the following:
apply from: "../../node_modules/react-native-vector-icons/fonts.gradle"
```

### API:
```bash
yarn add axios

# document:
https://viblo.asia/p/su-dung-axios-voi-react-1Je5E4zAlnL

# fix TypeError: Network request failed
adb reverse tcp:8000 tcp:8000
```

### Font:
```bash
# link fonts:
https://fonts.google.com/

# install:
yarn global add react-native-asset  # or: npm install -g react-native-asset

# create react-native.config.js and paste:
module.exports = {
    project: {
      ios: {},
      android: {},
    },
    assets: ['./src/fonts'],
};

# and run:
npx react-native-asset

# use: 
<Text style={{ fontFamily: '...' }}> ... </Text>
```
