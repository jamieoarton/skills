# Get Authorized Workspaces

View the Workspaces available to the authenticated user.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/team": {
      "get": {
        "summary": "Get Authorized Workspaces",
        "tags": [
          "Workspaces"
        ],
        "description": "View the Workspaces available to the authenticated user.",
        "operationId": "GetAuthorizedTeams",
        "parameters": [],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "GetAuthorizedTeamsresponse",
                  "required": [
                    "teams"
                  ],
                  "type": "object",
                  "properties": {
                    "teams": {
                      "type": "array",
                      "items": {
                        "title": "Team",
                        "required": [
                          "id",
                          "name",
                          "color",
                          "avatar",
                          "members"
                        ],
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          },
                          "color": {
                            "type": "string"
                          },
                          "avatar": {
                            "type": "string"
                          },
                          "members": {
                            "type": "array",
                            "items": {
                              "title": "Member",
                              "required": [
                                "user"
                              ],
                              "type": "object",
                              "properties": {
                                "user": {
                                  "$ref": "#/paths/~1v2~1user/get/responses/200/content/application~1json/schema/properties/user"
                                }
                              },
                              "examples": [
                                {
                                  "user": {
                                    "id": 123,
                                    "username": "John Doe",
                                    "color": "#000000",
                                    "profilePicture": "https://clickup.com/avatar.jpg"
                                  }
                                }
                              ]
                            },
                            "description": ""
                          }
                        },
                        "examples": [
                          {
                            "id": "1234",
                            "name": "My ClickUp Workspace",
                            "color": "#000000",
                            "avatar": "https://clickup.com/avatar.jpg",
                            "members": [
                              {
                                "user": {
                                  "id": 123,
                                  "username": "John Doe",
                                  "color": "#000000",
                                  "profilePicture": "https://clickup.com/avatar.jpg"
                                }
                              }
                            ]
                          }
                        ]
                      },
                      "description": ""
                    }
                  },
                  "examples": [
                    {
                      "teams": [
                        {
                          "id": "1234",
                          "name": "My ClickUp Workspace",
                          "color": "#000000",
                          "avatar": "https://clickup.com/avatar.jpg",
                          "members": [
                            {
                              "user": {
                                "id": 123,
                                "username": "John Doe",
                                "color": "#000000",
                                "profilePicture": "https://clickup.com/avatar.jpg"
                              }
                            }
                          ]
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "teams": [
                    {
                      "id": "1234",
                      "name": "My ClickUp Workspace",
                      "color": "#000000",
                      "avatar": "https://clickup.com/avatar.jpg",
                      "members": [
                        {
                          "user": {
                            "id": 123,
                            "username": "John Doe",
                            "color": "#000000",
                            "profilePicture": "https://clickup.com/avatar.jpg"
                          }
                        }
                      ]
                    }
                  ]
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Workspaces"
    }
  ]
}
```