# Edit Guest On Workspace

Configure options for a guest. \
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
    "/v2/team/{team_id}/guest/{guest_id}": {
      "put": {
        "summary": "Edit Guest On Workspace",
        "tags": [
          "Guests"
        ],
        "description": "Configure options for a guest. \\\n \\\n***Note:** This endpoint is only available to Workspaces on our [Enterprise Plan](https://clickup.com/pricing).*",
        "operationId": "EditGuestOnWorkspace",
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
          },
          {
            "name": "guest_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                403
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "EditGuestOnWorkspacerequest",
                "type": "object",
                "properties": {
                  "can_see_points_estimated": {
                    "type": "boolean"
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
                  "custom_role_id": {
                    "type": "integer",
                    "contentEncoding": "int32"
                  }
                },
                "examples": [
                  {
                    "can_see_points_estimated": true,
                    "can_edit_tags": true,
                    "can_see_time_spent": true,
                    "can_see_time_estimated": true,
                    "can_create_views": true,
                    "custom_role_id": 12345
                  }
                ]
              },
              "example": {
                "can_edit_tags": true,
                "can_see_time_spent": true,
                "can_see_time_estimated": true,
                "can_see_points_estimated": true,
                "can_create_views": true,
                "custom_role_id": 12345
              }
            }
          },
          "required": false
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "EditGuestOnWorkspaceresponse",
                  "required": [
                    "guest"
                  ],
                  "type": "object",
                  "properties": {
                    "guest": {
                      "title": "Guest",
                      "type": "object",
                      "properties": {
                        "user": {
                          "title": "User5",
                          "required": [
                            "id",
                            "username",
                            "email",
                            "color",
                            "profilePicture",
                            "initials",
                            "role",
                            "custom_role",
                            "last_active",
                            "date_joined",
                            "date_invited"
                          ],
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "username": {
                              "type": [
                                "string",
                                "null"
                              ]
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
                            "profilePicture": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "initials": {
                              "type": "string"
                            },
                            "role": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "custom_role": {
                              "$ref": "#/paths/~1v2~1team~1%7Bteam_id%7D~1user~1%7Buser_id%7D/get/responses/200/content/application~1json/schema/properties/member/properties/user/properties/custom_role"
                            },
                            "last_active": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "date_joined": {
                              "type": [
                                "string",
                                "null"
                              ]
                            },
                            "date_invited": {
                              "type": "string"
                            }
                          },
                          "examples": [
                            {
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
                            }
                          ]
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
                        "can_see_points_estimated": {
                          "type": "boolean"
                        },
                        "can_edit_tags": {
                          "type": "boolean"
                        },
                        "can_create_views": {
                          "type": "boolean"
                        },
                        "shared": {
                          "$ref": "#/paths/~1v2~1team~1%7Bteam_id%7D~1user~1%7Buser_id%7D/get/responses/200/content/application~1json/schema/properties/member/properties/shared"
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
                          "can_see_points_estimated": true,
                          "can_edit_tags": true,
                          "can_create_views": true,
                          "shared": {
                            "tasks": [],
                            "lists": [],
                            "folders": []
                          }
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "guest": {
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
                        "shared": {
                          "tasks": [],
                          "lists": [],
                          "folders": []
                        }
                      }
                    }
                  ]
                },
                "example": {
                  "guest": {
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
                    "can_see_points_estimated": true,
                    "shared": {
                      "tasks": [],
                      "lists": [],
                      "folders": []
                    }
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