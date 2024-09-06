# Dolphin Anty Automation with Selenium

This repository is created to automate proxy browsers of Dolphin Anty with Selenium. It provides functionalities to create, update, open, and delete browser profiles using a GUI built with Tkinter.

## Project Structure
```

```


### Files

- **[`main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\yanfe\OneDrive\Documentos\repo\Dolphin-Anty-Automation-with-Selenium\main.py")**: The main entry point of the application. It sets up the GUI and handles user interactions.
- **[`create_profile.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fcreate_profile.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\yanfe\OneDrive\Documentos\repo\Dolphin-Anty-Automation-with-Selenium\create_profile.py")**: Contains functions to create and update browser profiles via the Dolphin Anty API.
- **[`delete_browsers.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fdelete_browsers.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\yanfe\OneDrive\Documentos\repo\Dolphin-Anty-Automation-with-Selenium\delete_browsers.py")**: Contains functions to list and delete browser profiles.
- **[`open_profile.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fopen_profile.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\yanfe\OneDrive\Documentos\repo\Dolphin-Anty-Automation-with-Selenium\open_profile.py")**: Contains functions to open a browser profile using Selenium.
- **[`.env`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\yanfe\OneDrive\Documentos\repo\Dolphin-Anty-Automation-with-Selenium\.env")**: Stores environment variables such as the authentication token.
- **[`requirements.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\yanfe\OneDrive\Documentos\repo\Dolphin-Anty-Automation-with-Selenium\requirements.txt")**: Lists the dependencies required for the project.
- **[`LICENSE`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2FLICENSE%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\yanfe\OneDrive\Documentos\repo\Dolphin-Anty-Automation-with-Selenium\LICENSE")**: The license for the project.

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/dolphin-anty-automation.git
    cd dolphin-anty-automation
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    - Create a [`.env`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\yanfe\OneDrive\Documentos\repo\Dolphin-Anty-Automation-with-Selenium\.env") file in the root directory.
    - Add your authentication token to the [`.env`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\yanfe\OneDrive\Documentos\repo\Dolphin-Anty-Automation-with-Selenium\.env") file:
      ```
      AUTH_TOKEN=your_auth_token_here
      ```

4. **Run the application**:
    ```sh
    python main.py
    ```

## Usage

### GUI

The GUI allows you to create browser profiles by specifying the number of profiles and the proxies to be used. Each proxy should be in the format [`host:port:username:password`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cyanfe%5C%5COneDrive%5C%5CDocumentos%5C%5Crepo%5C%5CDolphin-Anty-Automation-with-Selenium%5C%5Cmain.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fmain.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A25%2C%22character%22%3A4%7D%7D%5D%5D "Go to definition") and listed one per line.

### Functions

- **[`create_profiles_in_bulk(profiles)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cyanfe%5C%5COneDrive%5C%5CDocumentos%5C%5Crepo%5C%5CDolphin-Anty-Automation-with-Selenium%5C%5Ccreate_profile.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fcreate_profile.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fcreate_profile.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A9%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cyanfe%5C%5COneDrive%5C%5CDocumentos%5C%5Crepo%5C%5CDolphin-Anty-Automation-with-Selenium%5C%5Cmain.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fmain.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A27%7D%7D%5D%5D "Go to definition")**: Creates multiple profiles in bulk.
- **`update_profile(profile_id, updated_data)`**: Updates an existing profile.
- **[`open_profile(profile_id)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cyanfe%5C%5COneDrive%5C%5CDocumentos%5C%5Crepo%5C%5CDolphin-Anty-Automation-with-Selenium%5C%5Cmain.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fmain.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A5%7D%7D%2C%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cyanfe%5C%5COneDrive%5C%5CDocumentos%5C%5Crepo%5C%5CDolphin-Anty-Automation-with-Selenium%5C%5Copen_profile.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fopen_profile.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fopen_profile.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A10%2C%22character%22%3A4%7D%7D%2C%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cyanfe%5C%5COneDrive%5C%5CDocumentos%5C%5Crepo%5C%5CDolphin-Anty-Automation-with-Selenium%5C%5CREADME.md%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2FREADME.md%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A6%2C%22character%22%3A2%7D%7D%5D%5D "Go to definition")**: Opens a browser profile using Selenium.
- **[`list_browsers()`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cyanfe%5C%5COneDrive%5C%5CDocumentos%5C%5Crepo%5C%5CDolphin-Anty-Automation-with-Selenium%5C%5Cmain.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fmain.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A28%7D%7D%5D%5D "Go to definition")**: Lists all browser profiles.
- **[`delete_browser(profile_id)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cyanfe%5C%5COneDrive%5C%5CDocumentos%5C%5Crepo%5C%5CDolphin-Anty-Automation-with-Selenium%5C%5Cmain.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fmain.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A43%7D%7D%5D%5D "Go to definition")**: Deletes a browser profile.

## Notes

- You need to have [`chromedriver`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cyanfe%5C%5COneDrive%5C%5CDocumentos%5C%5Crepo%5C%5CDolphin-Anty-Automation-with-Selenium%5C%5Copen_profile.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fopen_profile.py%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2Fopen_profile.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A31%2C%22character%22%3A75%7D%7D%2C%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22c%3A%5C%5CUsers%5C%5Cyanfe%5C%5COneDrive%5C%5CDocumentos%5C%5Crepo%5C%5CDolphin-Anty-Automation-with-Selenium%5C%5CREADME.md%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fc%253A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2FREADME.md%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2FREADME.md%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A22%2C%22character%22%3A17%7D%7D%5D%5D "Go to definition") to open profiles and use them with Selenium. It can be downloaded from Dolphin Anty's documentation.
  [Chrome driver download link](https://anty-browser.s3.amazonaws.com/chromedriver-124.zip)

- This project only includes basic CRUD operations for profiles. For more advanced usage, refer to the official documentation.

## License

This project is licensed under the MIT License. See the [`LICENSE`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2Fyanfe%2FOneDrive%2FDocumentos%2Frepo%2FDolphin-Anty-Automation-with-Selenium%2FLICENSE%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\yanfe\OneDrive\Documentos\repo\Dolphin-Anty-Automation-with-Selenium\LICENSE") file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or support, please open an issue in the repository.

## TODO:

falta pro lançamento:
- interface da rise
- autenticação com login e senha do bot
- subir a extenção pelo proprio bot via API do dolphin (pode ser ponto de melhoria)
- url de login inicial das plataformas para abrir os perfis direto na url certa
- ao finalizar o deve apagar os perfis e proxys

observações:
- vamos enviar o chrome-driver e a extenção junto aos arquivos do bot


AUTH_TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYWE4OGY3Njg4ZmUzYmRlOGQ1ODVkZmI3ODVjNWRiZjg1MmJlYzBhODEwMDg3YzdhODRjZmRkYzA4OWEzNTU0MDczNWFmNmVhYjQ1ZDU5NWQiLCJpYXQiOjE3MjQ2NDAxMjAuODc5OTE3LCJuYmYiOjE3MjQ2NDAxMjAuODc5OTE5LCJleHAiOjE3NTYxNzYxMjAuODcyMzY0LCJzdWIiOiIzNjg1MzcwIiwic2NvcGVzIjpbXX0.r2jVs3Vod-NPlqkT-ZZXdf5hZjK6U7EsBxz01RCKt9dLEkeLSNyK0jfbvdD-bzLjzsRWx7U2kScKpHFERH_Won3ZNRRBb1QddjmqWsavI12lBdzzO9mp1epe-h0sHQeSEjYeD0kcJt1MW7YSsDhT-IxYyxAArfHdjILJl-RrN2lt6lfZ84MmmtBpYLRKjXxaXl_wYciz_v20dA_gmp553ZnHvOfA47WDy_UEY7OjKC8WbnqVfZKaNvoWWEB9o4GePVvMQUkM2SjZWUvF1dPg4Y-8betvRm4cWcqqKtOI7z0tRtIG9Mv7xNAYr8h46Ew4_IJHNCkbsIcKJFgwvScbnABQARkrLbHzHC1qDgAcL3wLt_JAXDgsgFmHtAAAMcIyrOtq8o7o8BMJx-eiiGHB3IKnbqOtxQHp9D_estC-sd47vrV7c-r-eTOmuRL6lpNse_7689Rpm1hyvOvRXBi80UOObAeTS8OMOSz1rmpkpRnnaQHWKiJzCBPml9XJPf_P9ruNv_3DLNd1EsPjKEvAUKU1j2hZtfT7ana6_FqcILeUEylzqr48VNrpi1lV-_wGXczF8gNGxwg_Q5vOZVPwX5wvxgmPblMRGMvWY3I-5qimdgicpF9KtpW77yWMMKDN6IAeMA70IvTk2ybMOvXNKM2d1rjNpxJM3BPMokNmzrU