resource "github_repository" "yaml_replace" {
  name         = "yaml-replace"
  visibility   = "public"
  homepage_url = "https://pypi.org/project/yaml-replace/"
  topics = [
    "yaml",
    "yaml-parser",
    "substitute",
    "substitution",
    "replace",
    "replacement",
    "interpolation",
    "template",
    "template-engine"
  ]
  description     = "Parse yaml files with variables."
  has_downloads   = true
  has_issues      = true
  has_projects    = true
  has_wiki        = true
  has_discussions = false
}

resource "github_actions_secret" "pypi_username" {
  repository      = github_repository.yaml_replace.name
  secret_name     = "PYPI_USERNAME"
  plaintext_value = var.pypi_username
}

resource "github_actions_secret" "pypi_password" {
  repository      = github_repository.yaml_replace.name
  secret_name     = "PYPI_PASSWORD"
  plaintext_value = var.pypi_password
}

resource "github_actions_secret" "github_pat" {
  repository      = github_repository.yaml_replace.name
  secret_name     = "GH_PAT"
  plaintext_value = var.github_pat
}
