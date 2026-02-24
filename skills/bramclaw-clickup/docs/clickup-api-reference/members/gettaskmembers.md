# Get Task Members

Get Workspace members who have explicit access to a task. Responses do not include people with access through a Team, or people with access from the List, Folder, or Space where the task exists.

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
    "/v2/task/{task_id}/member": {
      "get": {
        "summary": "Get Task Members",
        "tags": [
          "Members"
        ],
        "description": "Get Workspace members who have explicit access to a task. Responses do not include people with access through a Team, or people with access from the List, Folder, or Space where the task exists.",
        "operationId": "GetTaskMembers",
        "parameters": [
          {
            "name": "task_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "9hz"
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "GetTaskMembersresponse",
                  "required": [
                    "members"
                  ],
                  "type": "object",
                  "properties": {
                    "members": {
                      "type": "array",
                      "items": {
                        "title": "Member5",
                        "required": [
                          "id",
                          "username",
                          "email",
                          "color",
                          "initials",
                          "profilePicture",
                          "profileInfo"
                        ],
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "integer",
                            "contentEncoding": "int32"
                          },
                          "username": {
                            "type": "string"
                          },
                          "email": {
                            "type": "string"
                          },
                          "color": {
                            "type": [
                              "string",
                              "null"
                            ]
                          },
                          "initials": {
                            "type": "string"
                          },
                          "profilePicture": {
                            "type": "string"
                          },
                          "profileInfo": {
                            "title": "ProfileInfo",
                            "required": [
                              "display_profile",
                              "verified_ambassador",
                              "verified_consultant",
                              "top_tier_user",
                              "viewed_verified_ambassador",
                              "viewed_verified_consultant",
                              "viewed_top_tier_user"
                            ],
                            "type": "object",
                            "properties": {
                              "display_profile": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "verified_ambassador": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "verified_consultant": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "top_tier_user": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "viewed_verified_ambassador": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "viewed_verified_consultant": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "viewed_top_tier_user": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              }
                            },
                            "examples": [
                              {
                                "display_profile": null,
                                "verified_ambassador": null,
                                "verified_consultant": null,
                                "top_tier_user": null,
                                "viewed_verified_ambassador": null,
                                "viewed_verified_consultant": null,
                                "viewed_top_tier_user": null
                              }
                            ]
                          }
                        },
                        "examples": [
                          {
                            "id": 812,
                            "username": "John Doe",
                            "email": "john@example.com",
                            "color": "#FFFFFF",
                            "initials": "JD",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/812_nx1.jpg",
                            "profileInfo": {
                              "display_profile": null,
                              "verified_ambassador": null,
                              "verified_consultant": null,
                              "top_tier_user": null,
                              "viewed_verified_ambassador": null,
                              "viewed_verified_consultant": null,
                              "viewed_top_tier_user": null
                            }
                          }
                        ]
                      },
                      "description": ""
                    }
                  },
                  "examples": [
                    {
                      "members": [
                        {
                          "id": 812,
                          "username": "John Doe",
                          "email": "john@example.com",
                          "color": "#FFFFFF",
                          "initials": "JD",
                          "profilePicture": "https://attachments-public.clickup.com/profilePictures/812_nx1.jpg",
                          "profileInfo": {
                            "display_profile": null,
                            "verified_ambassador": null,
                            "verified_consultant": null,
                            "top_tier_user": null,
                            "viewed_verified_ambassador": null,
                            "viewed_verified_consultant": null,
                            "viewed_top_tier_user": null
                          }
                        },
                        {
                          "id": 813,
                          "username": "Jane Doe",
                          "email": "jane@example.com",
                          "color": null,
                          "initials": "JD",
                          "profilePicture": "https://attachments-public.clickup.com/profilePictures/813_nx1.jpg",
                          "profileInfo": {
                            "display_profile": null,
                            "verified_ambassador": null,
                            "verified_consultant": null,
                            "top_tier_user": null,
                            "viewed_verified_ambassador": null,
                            "viewed_verified_consultant": null,
                            "viewed_top_tier_user": null
                          }
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "members": [
                    {
                      "id": 812,
                      "username": "John Doe",
                      "email": "john@example.com",
                      "color": "#FFFFFF",
                      "initials": "JD",
                      "profilePicture": "https://attachments-public.clickup.com/profilePictures/812_nx1.jpg",
                      "profileInfo": {
                        "display_profile": null,
                        "verified_ambassador": null,
                        "verified_consultant": null,
                        "top_tier_user": null,
                        "viewed_verified_ambassador": null,
                        "viewed_verified_consultant": null,
                        "viewed_top_tier_user": null
                      }
                    },
                    {
                      "id": 813,
                      "username": "Jane Doe",
                      "email": "jane@example.com",
                      "color": null,
                      "initials": "JD",
                      "profilePicture": "https://attachments-public.clickup.com/profilePictures/813_nx1.jpg",
                      "profileInfo": {
                        "display_profile": null,
                        "verified_ambassador": null,
                        "verified_consultant": null,
                        "top_tier_user": null,
                        "viewed_verified_ambassador": null,
                        "viewed_verified_consultant": null,
                        "viewed_top_tier_user": null
                      }
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
      "name": "Members"
    }
  ]
}
```