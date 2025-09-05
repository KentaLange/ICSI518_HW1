def main():
    search_query = "ytsearch2:street fighter 6"
    output_path = "/Users/kl/dev/HackaThonAgents%(title)s.%(ext)s"
    try:
        subprocess.run(["yt-dlp", "-o", output_path, search_query], check=True)
    except FileNotFoundError:
        print("yt-dlp is not installed or not found in PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"yt-dlp failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()