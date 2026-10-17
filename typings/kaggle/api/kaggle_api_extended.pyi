class ApiCompetitionFile:
    name: str
    total_bytes: int

class ApiListDataFilesResponse:
    files: list[ApiCompetitionFile]
    next_page_token: str

class KaggleApi:
    def authenticate(self) -> None: ...
    def competition_list_files(
        self,
        competition: str,
        page_token: str | None = None,
        page_size: int = 20,
    ) -> ApiListDataFilesResponse: ...
    def competition_download_files(
        self,
        competition: str,
        path: str | None = None,
        force: bool = False,
        quiet: bool = True,
    ) -> None: ...
    def dataset_download_files(
        self,
        dataset: str,
        path: str | None = None,
        force: bool = False,
        quiet: bool = True,
        unzip: bool = False,
        licenses: list[str] | None = None,
    ) -> None: ...
