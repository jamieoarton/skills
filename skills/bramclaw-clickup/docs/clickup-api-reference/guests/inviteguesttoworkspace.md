# Invite Guest To Workspace

Invite a guest to join a Workspace. To invite a member to your Workspace, use the [Invite User to Workspace](ref:inviteusertoworkspace) endpoint. \
 \
You'll also need to grant the guest access to specific items using the following endpoints: [Add Guest to Folder](ref:addguesttofolder), [Add Guest to List](ref:addguesttolist), or [Add Guest to Task](ref:addguesttotask). \
 \
***Note:** This endpoint is only available to Workspaces on our [Enterprise Plan](https://clickup.com/pricing).*

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
    "/v2/team/{team_id}/guest": {
      "post": {
        "summary": "Invite Guest To Workspace",
        "tags": [
          "Guests"
        ],
        "description": "Invite a guest to join a Workspace. To invite a member to your Workspace, use the [Invite User to Workspace](https://developer.clickup.com/reference/inviteusertoworkspace) endpoint. \\\n \\\nYou'll also need to grant the guest access to specific items using the following endpoints: [Add Guest to Folder](https://developer.clickup.com/reference/addguesttofolder), [Add Guest to List](https://developer.clickup.com/reference/addguesttolist), or [Add Guest to Task](https://developer.clickup.com/reference/addguesttotask). \\\n \\\n***Note:** This endpoint is only available to Workspaces on our [Enterprise Plan](https://clickup.com/pricing).*",
        "operationId": "InviteGuestToWorkspace",
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "InviteGuestToWorkspacerequest",
                "required": [
                  "email"
                ],
                "type": "object",
                "properties": {
                  "email": {
                    "type": "string"
                  },
                  "can_edit_tags": {
                    "type": "boolean"
                  },
                  "can_see_time_spent": {
                    "type": "boolean"
                  },
                  "can_see_time_estimated": {
                    "type": "boolean"
                  },
                  "can_create_views": {
                    "type": "boolean"
                  },
                  "can_see_points_estimated": {
                    "type": "boolean"
                  },
                  "custom_role_id": {
                    "type": "integer",
                    "contentEncoding": "int32"
                  }
                },
                "examples": [
                  {
                    "email": "guest@example.com",
                    "can_edit_tags": true,
                    "can_see_time_spent": true,
                    "can_see_time_estimated": true,
                    "can_create_views": true,
                    "can_see_points_estimated": true,
                    "custom_role_id": 12345
                  }
                ]
              },
              "example": {
                "email": "guest@example.com",
                "can_edit_tags": true,
                "can_see_time_spent": true,
                "can_see_time_estimated": true,
                "can_create_views": true,
                "custom_role_id": 12345
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "InviteGuestToWorkspaceresponse",
                  "required": [
                    "team"
                  ],
                  "type": "object",
                  "properties": {
                    "team": {
                      "title": "Team1",
                      "required": [
                        "id",
                        "name",
                        "color",
                        "avatar",
                        "members",
                        "roles"
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
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "members": {
                          "type": "array",
                          "items": {
                            "title": "Member4",
                            "required": [
                              "user",
                              "invited_by",
                              "can_see_time_spent",
                              "can_see_time_estimated",
                              "can_edit_tags",
                              "can_create_views"
                            ],
                            "type": "object",
                            "properties": {
                              "user": {
                                "$ref": "#/paths/~1v2~1team~1%7Bteam_id%7D~1guest~1%7Bguest_id%7D/put/responses/200/content/application~1json/schema/properties/guest/properties/user"
                              },
                              "invited_by": {
                                "$ref": "#/paths/~1v2~1team~1%7Bteam_id%7D~1user~1%7Buser_id%7D/get/responses/200/content/application~1json/schema/properties/member/properties/invited_by"
                              },
                              "can_see_time_spent": {
                                "type": "boolean"
                              },
                              "can_see_time_estimated": {
                                "type": "boolean"
                              },
                              "can_edit_tags": {
                                "type": "boolean"
                              },
                              "can_create_views": {
                                "type": "boolean"
                              },
                              "can_see_points_estimated": {
                                "type": "boolean"
                              }
                            },
                            "examples": [
                              {
                                "user": {
                                  "id": 184,
                                  "username": null,
                                  "email": "guest@example.com",
                                  "color": null,
                                  "profilePicture": null,
                                  "initials": "G",
                                  "role": 4,
                                  "custom_role": {
                                    "id": 12345,
                                    "name": "guest custom"
                                  },
                                  "last_active": null,
                                  "date_joined": null,
                                  "date_invited": "1583358383412"
                                },
                                "invited_by": {
                                  "id": 183,
                                  "color": "#827718",
                                  "username": "Jerry",
                                  "email": "jerry@example.com",
                                  "initials": "J",
                                  "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                                },
                                "can_see_time_spent": true,
                                "can_see_time_estimated": true,
                                "can_edit_tags": true,
                                "can_create_views": true,
                                "can_see_points_estimated": true
                              }
                            ]
                          },
                          "description": ""
                        },
                        "roles": {
                          "type": "array",
                          "items": {
                            "$ref": "#/paths/~1v2~1team~1%7Bteam_id%7D~1user/post/responses/200/content/application~1json/schema/properties/team/properties/roles/items"
                          },
                          "description": ""
                        }
                      },
                      "examples": [
                        {
                          "id": "333",
                          "name": "Team Name",
                          "color": "#8D00D4",
                          "avatar": null,
                          "members": [
                            {
                              "user": {
                                "id": 184,
                                "username": null,
                                "email": "guest@example.com",
                                "color": null,
                                "profilePicture": null,
                                "initials": "G",
                                "role": 4,
                                "custom_role": {
                                  "id": 12345,
                                  "name": "guest custom"
                                },
                                "last_active": null,
                                "date_joined": null,
                                "date_invited": "1583358383412"
                              },
                              "invited_by": {
                                "id": 183,
                                "color": "#827718",
                                "username": "Jerry",
                                "email": "jerry@example.com",
                                "initials": "J",
                                "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                              },
                              "can_see_time_spent": true,
                              "can_see_time_estimated": true,
                              "can_see_points_estimated": true,
                              "can_edit_tags": true,
                              "can_create_views": true
                            }
                          ],
                          "roles": [
                            {
                              "id": 1,
                              "name": "owner",
                              "custom": false
                            },
                            {
                              "id": 2,
                              "name": "admin",
                              "custom": false
                            },
                            {
                              "id": 3,
                              "name": "member",
                              "custom": false
                            },
                            {
                              "id": 4,
                              "name": "guest",
                              "custom": false
                            },
                            {
                              "id": 998877,
                              "name": "member custom",
                              "inherited_role": 3,
                              "custom": true
                            },
                            {
                              "id": 112233,
                              "name": "admin custom",
                              "inherited_role": 2,
                              "custom": true
                            },
                            {
                              "id": 12345,
                              "name": "guest custom",
                              "inherited_role": 4,
                              "custom": true
                            }
                          ]
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "team": {
                        "id": "333",
                        "name": "Team Name",
                        "color": "#8D00D4",
                        "avatar": null,
                        "members": [
                          {
                            "user": {
                              "id": 184,
                              "username": null,
                              "email": "guest@example.com",
                              "color": null,
                              "profilePicture": null,
                              "initials": "G",
                              "role": 4,
                              "custom_role": {
                                "id": 12345,
                                "name": "guest custom"
                              },
                              "last_active": null,
                              "date_joined": null,
                              "date_invited": "1583358383412"
                            },
                            "invited_by": {
                              "id": 183,
                              "color": "#827718",
                              "username": "Jerry",
                              "email": "jerry@example.com",
                              "initials": "J",
                              "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                            },
                            "can_see_time_spent": true,
                            "can_see_time_estimated": true,
                            "can_see_points_estimated": true,
                            "can_edit_tags": true,
                            "can_create_views": true
                          }
                        ],
                        "roles": [
                          {
                            "id": 1,
                            "name": "owner",
                            "custom": false
                          },
                          {
                            "id": 2,
                            "name": "admin",
                            "custom": false
                          },
                          {
                            "id": 3,
                            "name": "member",
                            "custom": false
                          },
                          {
                            "id": 4,
                            "name": "guest",
                            "custom": false
                          },
                          {
                            "id": 998877,
                            "name": "member custom",
                            "inherited_role": 3,
                            "custom": true
                          },
                          {
                            "id": 112233,
                            "name": "admin custom",
                            "inherited_role": 2,
                            "custom": true
                          },
                          {
                            "id": 12345,
                            "name": "guest custom",
                            "inherited_role": 4,
                            "custom": true
                          }
                        ]
                      }
                    }
                  ]
                },
                "example": {
                  "team": {
                    "id": "333",
                    "name": "Team Name",
                    "color": "#8D00D4",
                    "avatar": null,
                    "members": [
                      {
                        "user": {
                          "id": 184,
                          "username": null,
                          "email": "guest@example.com",
                          "color": null,
                          "profilePicture": null,
                          "initials": "G",
                          "role": 4,
                          "custom_role": {
                            "id": 12345,
                            "name": "guest custom"
                          },
                          "last_active": null,
                          "date_joined": null,
                          "date_invited": "1583358383412"
                        },
                        "invited_by": {
                          "id": 183,
                          "color": "#827718",
                          "username": "Jerry",
                          "email": "jerry@example.com",
                          "initials": "J",
                          "profilePicture": "https://attachments.clickup.com/profilePictures/profile.jpg"
                        },
                        "can_see_time_spent": true,
                        "can_see_time_estimated": true,
                        "can_edit_tags": true,
                        "can_create_views": true,
                        "can_see_points_estimated": true
                      }
                    ],
                    "roles": [
                      {
                        "id": 1,
                        "name": "owner",
                        "custom": false
                      },
                      {
                        "id": 2,
                        "name": "admin",
                        "custom": false
                      },
                      {
                        "id": 3,
                        "name": "member",
                        "custom": false
                      },
                      {
                        "id": 4,
                        "name": "guest",
                        "custom": false
                      },
                      {
                        "id": 998877,
                        "name": "member custom",
                        "inherited_role": 3,
                        "custom": true
                      },
                      {
                        "id": 112233,
                        "name": "admin custom",
                        "inherited_role": 2,
                        "custom": true
                      },
                      {
                        "id": 12345,
                        "name": "guest custom",
                        "inherited_role": 4,
                        "custom": true
                      }
                    ]
                  }
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
      "name": "Guests"
    }
  ]
}
```