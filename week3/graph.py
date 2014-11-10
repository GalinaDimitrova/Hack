class GitHubModule:
    def __init__(self):
        client_id = "296723c1e29fcce5133e"
        client_secret = "96e78dd0d7667c62e6c18570e242ca825ab98c3b"
        user ="Ivaylo-Bachvarov"
        auth =(client_id, client_secret)
        url = "https://api.github.com/users/{}/followers".format(user)
        #r = requests.get('https://api.github.com/users/whatever?client_id={}&client_secret={}'.format(client_id,client_secret))
        r = requests.get('https://api.github.com/users/whatever?client_id=xxxx&client_secret=yyyy', auth=auth)
        if r.status_code != 200:
            raise RuntimeError("Cannot access GitHub API from authentication")



def main():
    obj = GitHubModule()

if __name__ == '__main__':
    main()